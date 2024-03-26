<template>
    <el-container style="height: 100vh;">
        <!-- 顶部导航栏 -->
        <el-header class="header-menu">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
                <img style="width: 60px; margin-left: 2rem;" src="../../assets/img/logo_circle.ico" alt="logo" />
                <el-menu-item @click="GoIndex" index="1" style="font-weight: bold; margin-left: 3rem;"> 内 部 餐 饮 系 统 - 商
                    户 端
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
                            <span>首页</span>
                        </el-menu-item>
                        <el-sub-menu index="2">
                            <template #title>
                                <el-icon>
                                    <Document />
                                </el-icon>
                                <span>订单管理</span>
                            </template>
                            <el-menu-item index="2-1" @click="GoAddOrder">下单</el-menu-item>
                            <el-menu-item index="2-2" @click="GoOrder">订单管理</el-menu-item>
                        </el-sub-menu>
                        <el-menu-item index="3" @click="GoEmp">
                            <el-icon>
                                <Avatar />
                            </el-icon>
                            <span>雇员管理</span>
                        </el-menu-item>
                        <el-menu-item index="4" @click="GoDish">
                            <el-icon>
                                <DishDot />
                            </el-icon>
                            <span>菜品管理</span>
                        </el-menu-item>
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
                            <el-icon>
                                <Bowl />
                            </el-icon>
                            <span class="header-title">{{ userInfo.shop_name }}</span>
                            <div class="header-buttons">
                                <el-button type="primary" @click="dialogFormVisible = true; fillData()" :icon="Edit"
                                    circle />
                                <el-button type="danger" @click="dialogVisible2 = true" :icon="Delete" circle />
                            </div>
                        </div>
                    </template>
                    <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible2" title="敬告"
                        width="500">
                        <span>商户不支持自行注销账号，若有需求请联系管理员。</span>
                        <template #footer>
                            <div class="dialog-footer">
                                <el-button type="danger" @click="dialogVisible2 = false;">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <el-dialog style="margin-right: 58vh; margin-top: 25vh;" v-model="dialogFormVisible" title="修改资料"
                        width="500">
                        <el-form ref="ruleFormRef2" :model="form" :rules="rule2" label-width="20%" class="demo-form"
                                status-icon>
                            <el-form-item label="店铺名称" prop="shop_name">
                                <el-input v-model="form.shop_name" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="店长" prop="shop_head">
                                <el-input v-model="form.shop_head" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="联系电话" prop="shop_tel">
                                <el-input v-model="form.shop_tel" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="邀请码" prop="shop_pass">
                                <el-input v-model="form.shop_pass" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="电子邮件" prop="email">
                                <el-input v-model="form.email" autocomplete="off" />
                            </el-form-item>
                            <el-form-item label="店铺地址" prop="cus_address">
                                <el-input v-model="form.cus_address" autocomplete="off" />
                            </el-form-item>
                        </el-form>

                        <template #footer>
                            <div class="dialog-footer">
                                <el-button @click="dialogFormVisible = false; onReset(ruleFormRef2)">取消</el-button>
                                <el-button type="primary"
                                    @click="dialogFormVisible = false; updateInfo(userInfo.username, form)">
                                    确认
                                </el-button>
                            </div>
                        </template>
                    </el-dialog>
                    <p>{{ '登录账号： ' + userInfo.username }}</p><br>
                    <p>{{ '店长： ' + userInfo.shop_head }}</p><br>
                    <p>{{ '店铺电话： ' + userInfo.shop_tel }}</p><br>
                    <p>{{ '电子邮件： ' + userInfo.email }}</p><br>
                    <p>{{ '店铺地址： ' + userInfo.cus_address }}</p><br>

                    <template #footer>
                        <el-button type="success" @click="dialogVisible3 = true">查看邀请码</el-button>
                        <el-button type="warning" @click="dialogVisible = true">修改密码</el-button>
                        <el-dialog style="margin-right: 58vh; margin-top: 34vh;" v-model="dialogVisible" title="修改密码"
                            width="500">
                            <p>商户修改密码需要验证旧密码：</p><br>
                            <el-form ref="ruleFormRef" :model="form2" :rules="rule" label-width="20%" class="demo-form"
                                status-icon>
                                <el-form-item label="旧密码" prop="old_pass">
                                    <el-input type="password" v-model="form2.old_pass" />
                                </el-form-item>
                                <el-form-item label="新密码" prop="new_pass">
                                    <el-input type="password" v-model="form2.new_pass" />
                                </el-form-item>
                                <el-form-item label="确认密码" prop="re_pass">
                                    <el-input type="password" v-model="form2.re_pass" />
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
                        <el-dialog style="margin-right: 58vh; margin-top: 40vh;" v-model="dialogVisible3" title="查看邀请码"
                            width="500">
                            <span>发送链接与邀请码给新员工可快速添加员工到本店。</span><br><br>
                            <p>邀请码：{{ userInfo.shop_pass }}</p>
                            <template #footer>
                                <div class="dialog-footer">
                                    <el-button @click="dialogVisible3 = false">取消</el-button>
                                    <el-button type="success" @click="copyPass">
                                        复制到剪切板
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
import { $signout, $getMyInfo, $resetPass, $updateShop } from '@/api/shop';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore'
import {
    Delete, Edit, Bowl,
    Setting, HomeFilled,
    Document, Avatar, DishDot
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const username = useUserStore().getUsername
const userInfo = ref({})
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const dialogFormVisible = ref(false)
const ruleFormRef = ref()
const ruleFormRef2 = ref()

const form = reactive({
    shop_name: '',
    shop_head: '',
    shop_tel: '',
    shop_pass: '',
    email: '',
    cus_address: '',
})

const form2 = reactive({
    new_pass: '',
    old_pass: '',
    re_pass: ''
})

const validate_repass = (rule, value, callback) => {
    if (form2.re_pass === form2.new_pass) {
        callback();
    } else {
        callback(new Error('两次输入的新密码不一致'));
    }
}

const validate_email = (rule, value, callback) => {
    var emailRegExp = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
    var emailRegExp1 = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
    if ((!emailRegExp.test(value) && value != '') || (!emailRegExp1.test(value) && value != '')) {
        callback(new Error('请输入正确的邮箱格式'));
    } else {
        callback();
    }
}

const rule2 = reactive({
    shop_name: [
        { required: true, message: '店铺名称不能为空', trigger: 'blur' },
    ],
    shop_tel: [
        { required: true, message: '联系电话不能为空', trigger: 'blur' },
    ],
    shop_pass: [
        { required: true, message: '店铺邀请码不能为空', trigger: 'blur' },
    ],
    email: [
        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
        { validator: validate_email, message: '请输入正确的邮箱格式', trigger: ['blur'] }
    ],
})

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

const copyPass = () => {
    const protocol = window.location.protocol;
    const hostname = window.location.hostname;
    const port = window.location.port ? `:${window.location.port}` : '';
    const text = '【内部餐饮系统】' + userInfo.value.shop_name + ' 邀请您加入他们的团队，请点击链接完成加入：' + `${protocol}//${hostname}${port}` + '/#/joinShop' + '\n' + '邀请码：' + userInfo.value.shop_pass
    dialogVisible3.value = false
    navigator.clipboard.writeText(text).then(() => {
        alert('链接和邀请码已复制到剪切板！');
    }).catch(err => {
        alert('复制失败： ', err);
    });
}

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $resetPass(username, form2.old_pass, form2.new_pass)
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

const updateInfo = (username, form) => {
    $updateShop(username, form)
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
    form.shop_name = userInfo.value.shop_name;
    form.shop_head = userInfo.value.shop_head;
    form.shop_tel = userInfo.value.shop_tel;
    form.shop_pass = userInfo.value.shop_pass;
    form.email = userInfo.value.email;
    form.cus_address = userInfo.value.cus_address;
}

onMounted(() => {
    const savedUserInfo = localStorage.getItem('userInfo');
    if (savedUserInfo) {
        userInfo.value = JSON.parse(savedUserInfo);
    } else {
        getUser(username);
    }
})

const onReset = (formElRef) => {
    formElRef.resetFields();
}

const GoIndex = () => {
    router.push('/shop/index');
}
const GoAddOrder = () => {
    router.push('/shop/addOrder');
}
const GoOrder = () => {
    router.push('/shop/order');
}
const GoMe = () => {
    router.push('/shop/me');
}
const GoDish = () => {
    router.push('/shop/dish');
}
const GoEmp = () => {
    router.push('/shop/emp');
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