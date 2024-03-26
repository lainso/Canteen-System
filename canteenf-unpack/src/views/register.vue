<template>
    <div class="login">
        <img class="left" src="../assets/img/register_back.jpg" alt="left poster">
        <div class="box">
            <div class="logo-container">
                <img class="logo" src="../assets/img/logo.png" alt="left poster">
                <span class="logo-text">内部餐饮系统</span>
            </div>
            <div style="display: flex; text-align: center;">
                <p class="title">注册</p>
                <span class="regPart">已有账号？
                    <el-link :underline="false" type="primary" href="#login">前往登录</el-link>
                </span>
            </div>
            <el-form ref="ruleFormRef" :model="form" :rules="rules" label-width="20%" class="demo-form" status-icon>
                <el-form-item label="昵称" prop="name">
                    <el-input v-model="form.name" placeholder="取一个好听的名字吧~" />
                </el-form-item>
                <el-form-item label="登录账号" prop="username">
                    <el-input v-model="form.username" placeholder="请设置登录长账号，不可输入中文" />
                </el-form-item>
                <el-form-item label="登录密码" prop="password" style="margin-bottom: 5%;">
                    <el-input type="password" v-model="form.password" placeholder="请设置一个密码" />
                </el-form-item>
                <el-form-item label="电子邮件" prop="email">
                    <el-input v-model="form.email" placeholder="需要使用邮箱激活，注册后不可更改" />
                </el-form-item>
                <el-form-item label="联系电话" prop="tel">
                    <el-input v-model="form.tel" placeholder="请输入您的电话号码" />
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <el-select v-model="form.sex" placeholder="不可以是沃尔玛购物袋哦~">
                        <el-option label="男" value="男" />
                        <el-option label="女" value="女" />
                        <el-option label="保密" value="保密" />
                    </el-select>
                </el-form-item>
                <el-form-item label="生日">
                    <el-col>
                        <el-form-item prop="birth" style="margin-bottom: 0;">
                            <el-date-picker v-model="form.birth" type="date" label="生日" placeholder="选择一下你的生日吧~" />
                        </el-form-item>
                    </el-col>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit(ruleFormRef)">
                        注册
                    </el-button>
                    <el-button @click="onReset(ruleFormRef)">重置</el-button>
                </el-form-item>
            </el-form>
            <div class="info">
                <p>Copyright © 2024 lains. <span class="contact">Contact me ：<el-link :underline="false" type="success"
                            href="https://github.com/lainso" target="_blank">Github</el-link></span>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { $Register } from '@/api/customer';
import { useUserStore } from '@/stores/userStore'

const ruleFormRef = ref()
const userStore = useUserStore()

const form = reactive({
    username: '',
    password: '',
})

const validate_email = (rule, value, callback) => {
    var emailRegExp = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
    var emailRegExp1 = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/;
    if ((!emailRegExp.test(value) && value != '') || (!emailRegExp1.test(value) && value != '')) {
        callback(new Error('请输入正确的邮箱格式'));
    } else {
        callback();
    }
}

const rules = reactive({
    username: [
        { required: true, message: '登录账号不能为空', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '登录密码不能为空', trigger: 'blur' },
    ],
    name: [
        { required: true, message: '姓名不能为空', trigger: 'blur' },
    ],
    email: [
        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
        { validator: validate_email, message: '请输入正确的邮箱格式', trigger: ['blur'] }
    ],
})

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            // 提交注册逻辑
            $Register(form.username, form.password, form.name, form.email, form.sex, form.birth, form.tel)
                .then(function (data) {
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            // 传递username
            userStore.setUsername(form.username)
        } else {
            return false
        }
    })
}

const onReset = (formEl) => {
    if (!formEl) return
    formEl.resetFields()
}
</script>

<style scoped lang="scss">
.login {
    display: flex;
    align-items: center;
    height: 100vh;
    background-color: #f6f8fb;

    .left {
        width: 63%;
        height: 100vh;
        object-fit: cover;
    }

    .box {
        min-height: 755px;
        max-height: 100vh;
        width: 37%;
        padding: 4%;
        background: #f6f8fb;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
        border-radius: 4px;
        display: flex;
        justify-content: center;
        flex-direction: column;
        position: relative;

        .title {
            margin-bottom: 4%;
            padding-left: 21%;
            color: #303133;
            font-size: 3.5vh;
        }

        .regPart {
            margin-left: auto;
        }

        .logo-container {
            max-height: 20%;
            display: flex;
            align-items: center;
            margin-bottom: 5%;

            .logo {
                display: inline-block;
                max-height: 65px;
                border-radius: 50%;
            }

            .logo-text {
                display: inline-block;
                vertical-align: middle;
                margin-left: 5%;
                font-size: 5.5vh;
                font-family: Kai;
            }
        }

        .info {
            position: absolute;
            bottom: 1%;
            width: 80%;

            .contact {
                margin-left: auto;
            }
        }
    }
}

::v-deep .el-form-item__label {
    font-size: 16px;
}

::v-deep .el-form-item .el-input {
    height: 5.5vh;
    width: 47vh;

    .el-input__inner {
        font-size: 15px;
    }
}

::v-deep .el-form-item {
    margin-bottom: 7%;
}

::v-deep .el-button {
    height: 5vh;
    width: 19vh;
}

.login .box span,
.login .box p {
    display: flex;
    align-items: center;
}
</style>