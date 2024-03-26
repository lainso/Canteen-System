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
                            <span>支付卡注销</span>
                            <el-button @click="dialogVisible2 = true" type="danger">注销支付卡</el-button>
                        </div>
                    </template>
                    <div>
                        <p style="color: red;">⚠ ⚠ ⚠ ⚠ ⚠</p><br>请注意，注销支付卡为<span
                            style="color: red;">不可逆操作</span>！<br><br>请再三确认支付卡内余额已经使用完毕，注销后将<span
                            style="color: red;">无法找回</span>！<br><br>若需要退还余额，请根据流程向工作人员提出申请。<br><br>在您拿到退还金额之前，请<span
                            style="color: red;">不要进行注销操作</span>！
                    </div>
                    <template #footer><el-button @click="dialogVisible = true" type="primary"
                            plain>查看支付卡</el-button></template>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                        width="500">
                        <span>是否跳转到支付卡页面？</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible = false">取消</el-button>
                                <el-button type="primary" @click="dialogVisible = false; GoCardUpdate()">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible2" title="操作确认"
                        width="500">
                        <span>请输入您的卡号以确认注销。卡号可在支付卡详情中找到。</span><br><br>
                        <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="12%" class="demo-form"
                            status-icon>
                            <el-form-item label="卡号" prop="card_num">
                                <el-input v-model="form.card_num" />
                            </el-form-item>
                        </el-form>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                                <el-button type="danger" @click="delCard(ruleFormRef, form)">
                                    确认注销
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
import { ref, reactive } from 'vue';
import { $signout, $delCard } from '@/api/customer';
import { useRouter } from 'vue-router';
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
const form = reactive({
    card_num: ''
})

const delCard = (formEl, form) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $delCard(form.card_num)
                .then(function (data) {
                    alert("注销成功！")
                    onReset(ruleFormRef)
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            dialogVisible2.value = false;
        } else {
            return false
        }
    })
}

const rule = reactive({
    card_num: [
        { required: true, message: '卡号不能为空', trigger: 'blur' },
    ]
})

const onReset = (formElRef) => {
    if (!formElRef || !formElRef.value) return;
    formElRef.value.resetFields();
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
}
</style>