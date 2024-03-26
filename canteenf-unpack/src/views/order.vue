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
                    <el-menu default-active="2" class="el-menu-vertical-demo">
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
            <el-main>
                <el-row :gutter="20">
                    <el-card :body-style="{ padding: '20px' }" class="data-card"
                        style="width: 100%; max-width:800px; margin: 0 auto 1.5rem auto;">
                        <div>

                            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                                <el-form-item style="margin-left: 4rem;" label="筛选日期">
                                    <el-date-picker v-model="formInline.date" type="date" placeholder="开始日期"
                                        clearable />
                                    <span style="width: 2rem;"></span>
                                    <el-date-picker v-model="formInline.date2" type="date" placeholder="结束日期"
                                        clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="queryOrder">查询</el-button>
                                </el-form-item>
                            </el-form>
                            <h6 style="margin-left: 4rem; color: red;">*若要进行条件查询，请将两个条件都填写完整</h6>
                        </div>
                    </el-card>

                    <!-- 循环展现所有卡片，每个卡片独占一行且居中显示 -->
                    <el-col :span="24" v-for="card in cards" :key="card.title" style="margin-bottom: 20px;">
                        <el-card :body-style="{ padding: '20px' }" class="data-card"
                            style="width: 100%; max-width: 600px; margin: auto;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="flex-grow: 1;">
                                    <h4>消费时间：{{ fixTime(card.ord_time) }}</h4><br>
                                    <div>消费商店：{{ card.shop_name }}</div><br>
                                    <div>订单号：{{ card.ord_number }}</div><br>
                                    <div>订单金额：{{ card.ord_money }}</div><br>
                                    <div>订单状态：{{ card.ord_condition }}</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <!-- 分页组件 -->
                <div style="  display: flex; justify-content: center;">
                    <el-pagination v-model:current-page="currentPage1" :page-size="2" layout="prev, pager, next"
                        :total="totalOrders" @current-change="handleCurrentChange" />
                </div>

            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { $signout, $getOrderInfo } from '@/api/customer';
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
const currentPage1 = ref(1);
const cards = ref([]);
const totalOrders = ref(0);
const username = useUserStore().getUsername

const getOrder = (username, s_time, e_time, pagenum) => {
    $getOrderInfo(username, s_time, e_time, 2, pagenum)
    .then(function (response) {
        cards.value = response.data;
        totalOrders.value = response.total;
    })
    .catch(function (error) {
        console.log(error);
    });
}

onMounted(() => {
    getOrder(username, formInline.date, formInline.date2, currentPage1.value);
});

const fixTime = (time) => {
    if (time === null || time === '') {
        return '';
    } else {
        const date = new Date(time);
        date.setHours(date.getHours());
        const year = date.getFullYear();
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const day = date.getDate().toString().padStart(2, '0');
        return `${year}-${month}-${day}`
    }
}

const handleCurrentChange = (val) => {
    getOrder(username, formInline.date, formInline.date2, val)
}

const queryOrder = () => {
    getOrder(username, formInline.date, formInline.date2, 1);
};

const formInline = reactive({
    date: '',
    date2: '',
})


const signout = () => {
    $signout()
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
};

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
</style>