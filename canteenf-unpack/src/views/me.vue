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
                    <el-menu default-active="5" class="el-menu-vertical-demo">
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
                            <el-icon v-if="userInfo.cus_sex === '男'">
                                <Male />
                            </el-icon>
                            <el-icon v-else-if="userInfo.cus_sex === '女'">
                                <Female />
                            </el-icon>
                            <el-icon v-else>
                                <Minus />
                            </el-icon>
                            <span class="header-title">{{ userInfo.first_name }}</span>
                            <div class="header-buttons">
                                <el-button type="primary" @click="dialogFormVisible = true; fillData()" :icon="Edit"
                                    circle />
                                <el-button type="danger" @click="dialogVisible2 = true" :icon="Delete" circle />
                            </div>
                        </div>
                    </template>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible2" title="操作确认"
                        width="500">
                        <span>此操作不可逆！是否确认删除账号？</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogVisible2 = false">取消</el-button>
                                <el-button type="danger" @click="dialogVisible2 = false; delCustomer(userInfo.id)">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <el-dialog style="margin-right: 58vh; margin-top: 29vh;" v-model="dialogFormVisible" title="修改资料"
                        width="500">
                        <el-form :model="form">
                            <el-form-item required label="姓名" :label-width="formLabelWidth">
                                <el-input v-model="form.fname" autocomplete="off" />
                            </el-form-item>
                            <el-form-item required label="电话" :label-width="formLabelWidth">
                                <el-input v-model="form.tel" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="地址" :label-width="formLabelWidth">
                                <el-input v-model="form.address" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="性别" :label-width="formLabelWidth">
                                <el-select v-model="form.sex">
                                    <el-option label="男" value="男" />
                                    <el-option label="女" value="女" />
                                    <el-option label="保密" value="保密" />
                                </el-select>
                            </el-form-item>
                            <el-form-item label="生日" :label-width="formLabelWidth">
                                <el-date-picker v-model="form.birth" style="width: 100%;" type="date" label="生日" />
                            </el-form-item>
                        </el-form>

                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogFormVisible = false">取消</el-button>
                                <el-button type="primary"
                                    @click="dialogFormVisible = false; updateCustomer(userInfo.id, form)">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <p>{{ '登录账号： ' + userInfo.username }}</p><br>
                    <p>{{ '电子邮件： ' + userInfo.email }}</p><br>
                    <p>{{ '联系电话： ' + userInfo.cus_tel }}</p><br>
                    <p>{{ '生日： ' + fixTime(userInfo.cus_birth) }}</p><br>
                    <p>{{ '地址： ' + fixAddress(userInfo.cus_address) }}</p><br>

                    <template #footer> <el-button type="warning" @click="dialogVisible = true">修改密码</el-button>
                        <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                            width="500">
                            <span>是否确认修改密码？</span>
                            <template #footer>
                                <div class="dialog-footer">
                                    <el-button @click="dialogVisible = false">取消</el-button>
                                    <el-button type="warning"
                                        @click="dialogVisible = false; updatePass(userInfo.email)">
                                        确认
                                    </el-button>
                                </div>
                            </template>
                        </el-dialog>
                    </template>
                </el-card>
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import { $signout, $getMyInfo, $delCus, $updateCus } from '@/api/customer';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore'
import { $resetPass } from '@/api/customer';
import { useEmailStore } from '@/stores/emailStore'
import {
    Delete, Edit, Document,
    ChatDotSquare, Minus,
    CreditCard, Male, Female,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const username = useUserStore().getUsername
const userInfo = ref({})
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogFormVisible = ref(false)
const emailStore = useEmailStore()
const formLabelWidth = '60px'

const form = reactive({
    fname: '',
    tel: '',
    sex: '',
    birth: '',
    address: '',
})

const updateCustomer = (id, form) => {
    $updateCus(id, form)
        .then(function (data) {
            console.log(data);
            if (confirm("提交成功，新信息将在下次登录后更新！是否重新登录？")) {
                signout()
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const delCustomer = (id) => {
    $delCus(id)
        .then(function (data) {
            console.log(data);
            signout()
        })
        .catch(function (error) {
            console.log(error);
        });
}

const updatePass = (email) => {
    $resetPass(email)
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
    emailStore.setEmail(email)
    signout()
}

const fixTime = (time) => {
    const date = new Date(time);
    date.setHours(date.getHours());
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');

    return `${year}-${month}-${day}`;
}

const fixAddress = (address) => {
    if (address === null) {
        return '未填写'
    } else {
        return address
    }
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

const fillData = () => {
    form.fname = userInfo.value.first_name;
    form.tel = userInfo.value.cus_tel;
    form.address = userInfo.value.cus_address;
    form.sex = userInfo.value.cus_sex;
    form.birth = userInfo.value.cus_birth;
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
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
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