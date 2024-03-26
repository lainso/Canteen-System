<template>
    <el-container style="height: 100vh;">
        <!-- 顶部导航栏 -->
        <el-header class="header-menu">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
                <img style="width: 60px; margin-left: 2rem;" src="../../assets/img/logo_circle.ico" alt="logo" />
                <el-menu-item @click="GoIndex" index="1" style="font-weight: bold; margin-left: 3rem;"> 内 部 餐 饮 系 统 - 管 理 员 端
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
                    <el-menu default-active="1" class="el-menu-vertical-demo">
                        <el-menu-item index="1" @click="GoIndex">
                            <el-icon>
                                <HomeFilled />
                            </el-icon>
                            <span>首页</span>
                        </el-menu-item>
                        <el-menu-item index="2" @click="GoCus">
                            <el-icon><Avatar /></el-icon>
                            <span>账户管理</span>
                        </el-menu-item>
                        <el-sub-menu index="3">
                            <template #title>
                                <el-icon><ForkSpoon /></el-icon>
                                <span>商户管理</span>
                            </template>
                            <el-menu-item index="3-1" @click="GoShop">商户</el-menu-item>
                            <el-menu-item index="3-2" @click="GoEmp">雇员</el-menu-item>
                            <el-menu-item index="3-3" @click="GoDish">菜品</el-menu-item>
                        </el-sub-menu>

                        <el-sub-menu index="4">
                            <template #title>
                                <el-icon>
                                    <Document />
                                </el-icon>
                                <span>订单管理</span>
                            </template>
                            <el-menu-item index="4-1" @click="GoOrder">订单</el-menu-item>
                            <el-menu-item index="4-2" @click="GoPayment">支付记录</el-menu-item>
                        </el-sub-menu>
                        <el-menu-item index="5" @click="GoNoti">
                            <el-icon>
                                <ChatDotSquare />
                            </el-icon>
                            <span>通知管理</span>
                        </el-menu-item>
                        <el-menu-item index="6" @click="GoCard">
                            <el-icon>
                                <CreditCard />
                            </el-icon>
                            <span>支付卡管理</span>
                        </el-menu-item>
                        
                        <el-menu-item index="7" @click="GoPromo">
                            <el-icon><DocumentChecked /></el-icon>
                            <span>促销管理</span>
                        </el-menu-item>
                        <el-sub-menu index="8">
                            <template #title>
                                <el-icon>
                                    <setting />
                                </el-icon>
                                <span>账 号 设 置</span>
                            </template>
                            <el-menu-item index="8-1" @click="GoMe">个 人 中 心</el-menu-item>
                            <el-menu-item index="8-2" @click="signout">退 出 账 号</el-menu-item>
                        </el-sub-menu>
                    </el-menu>
                </el-col>
            </el-row>

            <!-- 主体内容 -->
            <el-main>
                <div style="max-width: 700px; margin: auto;">
                    <br><br>
                    <p style="text-align: center; font-size: 24px;">尊敬的管理员 {{ userInfo.first_name }}，欢迎登录内部餐饮系统！</p>
                    <br><br>
                    <div class="block text-center" m="t-4">
                        <el-carousel trigger="click" height="300px" motion-blur="true">
                            <el-carousel-item>
                                <img class="banner" src="../../assets/img/super/main_banner1.jpg">
                            </el-carousel-item>
                            <el-carousel-item>
                                <img class="banner" src="../../assets/img/super/main_banner2.jpg">
                            </el-carousel-item>
                            <el-carousel-item>
                                <img class="banner" src="../../assets/img/super/main_banner3.jpg">
                            </el-carousel-item>
                            <el-carousel-item>
                                <img class="banner" src="../../assets/img/super/main_banner4.jpg">
                            </el-carousel-item>
                        </el-carousel>
                    </div><br><br>
                    <p style="text-align: center; font-size: 20px;">现在时间是：{{ currentDate }} {{ currentTime }}<br><br>
                    </p>
                    <p style="text-align: center; font-size: 20px;">唯有爱和美食不可辜负😘</p><br>
                    <div style="text-align: center; padding: 20px;">
                        <p style="font-size: 16px;">您上次的登录时间为 {{ fixTime(userInfo.last_login) }}<br>如发现异常，请及时修改密码，以防资金损失
                        </p>
                    </div>
                </div>
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { $signout } from '@/api/super';
import { $getMyInfo } from '@/api/customer';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore'
import {
    Document, Avatar, ForkSpoon,
    ChatDotSquare, DocumentChecked,
    CreditCard,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const username = useUserStore().getUsername
const userInfo = ref({})
const currentDate = ref(new Date().toLocaleDateString())
const currentTime = ref(new Date().toLocaleTimeString())

setInterval(() => {
    currentDate.value = new Date().toLocaleDateString()
    currentTime.value = new Date().toLocaleTimeString()
}, 1000)

const fixTime = (time) => {
    const date = new Date(time);
    date.setHours(date.getHours());

    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');

    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

const getUser = (username) => {
    $getMyInfo(username)
        .then(function (data) {
            userInfo.value = data;
            localStorage.setItem('userInfo', JSON.stringify(data));
        })
        .catch(function (error) {
            console.log(error);
        });
}

onMounted(() => {
    const savedUserInfo = localStorage.getItem('userInfo');
    if (savedUserInfo) {
        userInfo.value = JSON.parse(savedUserInfo);
    } else {
        getUser(username);
    }
})

const GoIndex = () => {
    router.push('/super/index');
}
const GoOrder = () => {
    router.push('/super/order');
}
const GoNoti = () => {
    router.push('/super/noti');
}
const GoCard = () => {
    router.push('/super/paycard');
}
const GoMe = () => {
    router.push('/super/me');
}
const GoPayment = () => {
    router.push('/super/payment');
}
const GoDish = () => {
    router.push('/super/dish');
}
const GoEmp = () => {
    router.push('/super/emp');
}
const GoShop = () => {
    router.push('/super/shop');
}
const GoPromo = () => {
    router.push('/super/promo');
}
const GoCus = () => {
    router.push('/super/customer');
}

const signout = () => {
    localStorage.removeItem('userInfo')
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

.demonstration {
    color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

.banner {
    object-fit: cover;
    height: 300px;
    width: 100%;
}
</style>