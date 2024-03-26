<template>
    <el-container style="height: 100vh;">
        <!-- 顶部导航栏 -->
        <el-header class="header-menu">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
                <img style="width: 60px; margin-left: 2rem;" src="../assets/img/logo_circle.ico" alt="logo" />
                <el-menu-item @click="GoIndex" index="1" style="font-weight: bold; margin-left: 3rem;"> 内 部 餐 饮 系 统
                </el-menu-item>
                <div class="flex-grow" />
                <el-menu-item index="2" @click="signout">退 出 登 录</el-menu-item>
            </el-menu>
        </el-header>

        <!-- 页面主体 -->
        <el-container>
            <!-- 左侧边栏 -->
            <el-row class="tac">
                <el-col :span="24">
                    <br>
                    <el-menu default-active="4" class="el-menu-vertical-demo">
                        <el-menu-item index="1" @click="GoIndex">
                            <el-icon>
                                <HomeFilled />
                            </el-icon>
                            <span>首 页</span>
                        </el-menu-item>
                        <el-menu-item index="2" @click="GoOrder">
                            <el-icon>
                                <document />
                            </el-icon>
                            <span>订 单</span>
                        </el-menu-item>
                        <el-menu-item index="3" @click="GoNoti">
                            <el-icon>
                                <ChatDotSquare />
                            </el-icon>
                            <span>通 知</span>
                        </el-menu-item>
                        <el-sub-menu index="4">
                            <template #title>
                                <el-icon>
                                    <CreditCard />
                                </el-icon>
                                <span>支 付 卡</span>
                            </template>
                            <el-menu-item index="4-1" @click="GoCardApply">申 请</el-menu-item>
                            <el-menu-item index="4-2" @click="GoCardUpdate">储 值</el-menu-item>
                            <el-menu-item index="4-3" @click="GoCardDel">注 销</el-menu-item>
                        </el-sub-menu>
                        <el-sub-menu index="5">
                            <template #title>
                                <el-icon>
                                    <setting />
                                </el-icon>
                                <span>账 号 设 置</span>
                            </template>
                            <el-menu-item index="5-1" @click="GoMe">个 人 中 心</el-menu-item>
                            <el-menu-item index="5-2" @click="signout">退 出 账 号</el-menu-item>
                        </el-sub-menu>
                    </el-menu>
                </el-col>
            </el-row>

            <!-- 主体内容 -->
            <el-main style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <el-card class="box-card" shadow="hover">
                    <template #header>
                        <div class="card-header">
                            <span>支付卡管理</span>
                            <el-button @click="dialogVisible2 = true" type="success">开始储值</el-button>
                        </div>
                    </template>
                    <div>
                        <p>登录账户：{{ username }}</p><br>
                        <!-- 下方报错 -->
                        <p>支付卡卡号：{{ cardInfo.card_number }}</p><br>
                        <p>支付卡状态：{{ cardInfo.card_condition }}</p><br>
                        <p>支付卡余额：{{ cardInfo.card_balance }}</p>
                    </div>
                    <template #footer><el-button @click="dialogVisible = true" type="primary"
                            plain>查看消费明细</el-button></template>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                        width="500">
                        <span>是否跳转到订单页面？</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible = false">取消</el-button>
                                <el-button type="primary" @click="dialogVisible = false; GoOrder()">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <el-dialog style="margin-right: 58vh; margin-top: 25vh;" v-model="dialogVisible2" title="提交储值"
                        width="500">
                        <span><br>请注意，此支付卡<span style="color: red;">仅在本系统使用</span>，无法应用于其它系统。<br><br>一旦储值成功，将<span style="color: red;">无法退回</span>，只能在本系统内消费。<br><br>请妥善保管您的支付卡，遗失后补办将<span style="color: red;">丢失原卡内所有余额</span>。<br><br>填写正确的优惠码可获得储值优惠，优惠码可从系统通知等多渠道获取。<br><br>请输入您需要储值的金额：</span><br><br>
                        <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="15%" class="demo-form"
                            status-icon>
                            <el-form-item label="金额" prop="card_money">
                                <el-input v-model="form.card_money" />
                            </el-form-item>
                            <el-form-item label="优惠码" prop="promo_code">
                                <el-input v-model="form.promo_code" />
                            </el-form-item>
                        </el-form>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                                <el-button type="success" @click="updateCard(ruleFormRef, form)">
                                    确认储值
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                </el-card>
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { $signout, $updateCard, $getCardInfo } from '@/api/customer';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore'
import {
    Document,
    ChatDotSquare,
    CreditCard,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const ruleFormRef = ref()
const cardInfo = ref({})
const username = useUserStore().getUsername
const form = reactive({
    card_money: '',
    promo_code: ''
})

const getCard = (username) => {
    $getCardInfo(username)
        .then(function (data) {
            cardInfo.value = data;
            console.log(cardInfo)
            localStorage.setItem('cardInfo', JSON.stringify(data));
        })
        .catch(function (error) {
            console.log(error);
        });
}

onMounted(() => {
    const savedCardInfo = localStorage.getItem('cardInfo');
    if (savedCardInfo && savedCardInfo !== 'undefined') {
        cardInfo.value = JSON.parse(savedCardInfo);
    } else {
        getCard(username);
    }
});

const updateCard = (formEl, form) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            if (form.card_money > 0) {
                $updateCard(cardInfo.value.card_number, form.card_money, form.promo_code)
                    .then(function (data) {
                        alert("提交成功，余额将在下次登录后更新！")
                        onReset(ruleFormRef)
                        console.log(data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                dialogVisible2.value = false;
            } else {
                alert("金额必须是正数！");
            }
        } else {
            return false
        }
    })
}

const rule = reactive({
    card_money: [
        { required: true, message: '储值金额不能为空', trigger: 'blur' },
    ]
})

const onReset = (formElRef) => {
    formElRef.resetFields();
}

const GoIndex = () => {
    router.push('/index');
}
const GoOrder = () => {
    router.push('/order');
}
const GoNoti = () => {
    router.push('/noti');
}
const GoCardApply = () => {
    router.push('/cardApply');
}
const GoCardUpdate = () => {
    router.push('/cardUpdate');
}
const GoCardDel = () => {
    router.push('/cardDel');
}
const GoMe = () => {
    router.push('/me');
}

const signout = () => {
    $signout()
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
};
</script>
<style scoped>
el-main {
    padding-bottom: 2rem;
}

.el-col {
    display: flex;
    justify-content: center;
}

.data-card {
    transition: box-shadow .3s;
    cursor: pointer;
}

.data-card:hover {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.flex-grow {
    flex-grow: 1;
}

el-container {
    height: calc(100vh - 84px);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.text {
    font-size: 14px;
}

.item {
    margin-bottom: 18px;
}

.box-card {
    width: 480px;
}</style>