<template>
    <el-container style="height: 100vh;">
        <!-- 顶部导航栏 -->
        <el-header class="header-menu">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
                <img style="width: 60px; margin-left: 2rem;" src="../../assets/img/logo_circle.ico" alt="logo" />
                <el-menu-item @click="GoIndex" index="1" style="font-weight: bold; margin-left: 3rem;"> 内 部 餐 饮 系 统 - 管
                    理 员 端
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
                    <el-menu default-active="8" class="el-menu-vertical-demo">
                        <el-menu-item index="1" @click="GoIndex">
                            <el-icon>
                                <HomeFilled />
                            </el-icon>
                            <span>首页</span>
                        </el-menu-item>
                        <el-menu-item index="2" @click="GoCus">
                            <el-icon>
                                <Avatar />
                            </el-icon>
                            <span>账户管理</span>
                        </el-menu-item>
                        <el-sub-menu index="3">
                            <template #title>
                                <el-icon>
                                    <ForkSpoon />
                                </el-icon>
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
                            <el-icon>
                                <DocumentChecked />
                            </el-icon>
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
                    <el-dialog style="margin-right: 58vh; margin-top: 42vh;" v-model="dialogVisible2" title="删除账号"
                        width="500">
                        <span>管理员不支持删除账号。若需要增强安全性，请考虑修改密码。</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button type="danger" @click="dialogVisible2 = false;">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <p>{{ '登录账号： ' + userInfo.username }}</p><br>
                    <p>{{ '电子邮件： ' + userInfo.email }}</p><br>
                    <p>{{ '联系电话： ' + userInfo.cus_tel }}</p><br>
                    <template #footer> <el-button type="warning" @click="dialogVisible = true">修改密码</el-button>
                        <el-dialog style="margin-right: 58vh; margin-top: 35vh;" v-model="dialogVisible" title="修改密码"
                            width="500">
                            <p>管理员修改密码需要验证旧密码：</p><br>
                            <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="20%" class="demo-form"
                                status-icon>
                                <el-form-item label="旧密码" prop="old_pass">
                                    <el-input type="password" v-model="form.old_pass" />
                                </el-form-item>
                                <el-form-item label="新密码" prop="new_pass">
                                    <el-input type="password" v-model="form.new_pass" />
                                </el-form-item>
                                <el-form-item label="确认密码" prop="re_pass">
                                    <el-input type="password" v-model="form.re_pass" />
                                </el-form-item>
                            </el-form>
                            <template #footer>
                                <div class="dialog-footer">
                                    <el-button @click="dialogVisible = false; onReset(ruleFormRef)">取消</el-button>
                                    <el-button type="warning" @click=" onSubmit(ruleFormRef)">
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
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore'
import { $signout, $resetPass } from '@/api/super';
import { $getMyInfo, $updateCus } from '@/api/customer';
import {
    Delete, Edit, Document,
    ChatDotSquare, Minus,
    CreditCard, Male, Female,
    Setting, HomeFilled,
    Avatar, ForkSpoon,
    DocumentChecked
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const ruleFormRef = ref()
const userInfo = ref({})
const username = useUserStore().getUsername
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogFormVisible = ref(false)
const formLabelWidth = '60px'

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

const fillData = () => {
    form.fname = userInfo.value.first_name;
    form.tel = userInfo.value.cus_tel;
    form.address = userInfo.value.cus_address;
    form.sex = userInfo.value.cus_sex;
    form.birth = userInfo.value.cus_birth;
}

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $resetPass(username, form.old_pass, form.new_pass)
                .then(function (data) {
                    alert('修改密码成功，请重新登录！')
                    console.log(data);
                    dialogVisible.value = false;
                    signout()
                })
                .catch(function (error) {
                    console.log(error);
                });
        } else {
            return false
        }
    })
}

const getInfo = () => {
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
    console.log(userInfo.value);
})

const fixTime = (time) => {
    const date = new Date(time);
    date.setHours(date.getHours());
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');

    return `${year}-${month}-${day}`;
}

const form = reactive({
    new_pass: '',
    old_pass: '',
    re_pass: ''
})

const validate_repass = (rule, value, callback) => {
    if (value === form.new_pass) {
        callback();
    } else {
        callback(new Error('两次输入的新密码不一致'));
    }
}

const rule = reactive({
    old_pass: [
        { required: true, message: '旧密码不能为空', trigger: 'blur' },
    ],
    new_pass: [
        { required: true, message: '新密码不能为空', trigger: 'blur' },
    ],
    re_pass: [
        { required: true, message: '请再次输入新密码', trigger: 'blur' },
        { validator: validate_repass, message: '两次输入的新密码不一致', trigger: ['blur'] }
    ],
})

const onReset = (formElRef) => {
    formElRef.resetFields();
}

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