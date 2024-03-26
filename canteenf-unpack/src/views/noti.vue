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
                    <el-menu default-active="3" class="el-menu-vertical-demo">
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
                    <!-- 循环展现所有卡片，每个卡片独占一行且居中显示 -->
                    <el-col :span="24" v-for="card in cards" :key="card.title" style="margin-bottom: 20px;">
                        <el-card :body-style="{ padding: '20px' }" class="data-card"
                            style="width: 100%; max-width: 600px; margin: auto;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="flex-grow: 1;">
                                    <h4>{{ card.noti_title }}</h4><br>
                                    <div>{{ card.noti_content }}</div><br>
                                    <div>发送时间：{{ fixTime(card.noti_sendtime) }}</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <!-- 分页组件 -->
                <div style="  display: flex; justify-content: center;">
                    <el-pagination v-model:current-page="currentPage1" :page-size="4" layout="prev, pager, next"
                        :total="totalNotis" @current-change="handleCurrentChange" />
                </div>
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { $signout, $getNotiInfo } from '@/api/customer';
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
const totalNotis = ref(0);
const username = useUserStore().getUsername

const getNoti = (username, pagenum) => {
    $getNotiInfo(username, 4, pagenum)
        .then(function (response) {
            const newCards = response.data.map(item => {
                return {
                    noti_title: item.fields.noti_title || '',
                    noti_content: item.fields.noti_content || '',
                    noti_sendtime: item.fields.noti_sendtime || ''
                };
            });
            cards.value = newCards;
            totalNotis.value = response.total;
        })
        .catch(function (error) {
            console.log(error);
        });
}

onMounted(() => {
    getNoti(username, currentPage1.value);
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
    getNoti(username, val)
    console.log(val)
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