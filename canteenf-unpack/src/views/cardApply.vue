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
                            <span>支付卡申请</span>
                            <el-button @click="dialogVisible2 = true" type="success">立即申请</el-button>
                        </div>
                    </template>
                    <div>
                        <p style="color: orange;">⚠ ⚠ ⚠ ⚠ ⚠</p><br>请注意，此支付卡<span
                            style="color: red;">仅在本系统使用</span>，无法应用于其它系统。<br><br>填写申请后，工作人员将在7个工作日内交付支付卡。<br><br>请妥善保管您的支付卡，遗失后补办将<span
                            style="color: red;">丢失原卡内所有余额</span>。<br><br>最后请再三确认您的个人信息，以避免不必要的麻烦。
                    </div>
                    <template #footer><el-button @click="dialogVisible = true" type="warning" plain>确认个人信息</el-button></template>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                        width="500">
                        <span>是否跳转到账户信息页面？</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible = false">取消</el-button>
                                <el-button type="warning" @click="dialogVisible = false; GoMe()">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible2" title="操作确认"
                        width="500">
                        <span>我已阅读并知晓相关注意事项。</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible2 = false">取消</el-button>
                                <el-button type="success" @click="dialogVisible2 = false; applyCard(username)">
                                    确认申请
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
import { ref } from 'vue';
import { $signout, $applyCard } from '@/api/customer';
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
const username = useUserStore().getUsername

const applyCard = (username) => {
    $applyCard(username)
        .then(function (data) {
            console.log(data);
            alert("申请成功！请前往邮箱查收激活邮件。")
            router.push('/cardActive');
        })
        .catch(function (error) {
            console.log(error);
        });
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