<template>
    <div class="login">
        <img class="left" src="../assets/img/resetPass_back.jpg" alt="left poster">
        <div class="box">
            <div class="logo-container">
                <img class="logo" src="../assets/img/logo.png" alt="left poster">
                <span class="logo-text">内部餐饮系统</span>
            </div>
            <div style="display: flex; text-align: center;">
                <p class="title">密码重置</p>
                <span class="regPart">
                    <el-link :underline="false" type="primary" href="#login">返回登录</el-link>
                </span>
            </div>
            <el-form ref="ruleFormRef" :model="form" :rules="rules" label-width="20%" class="demo-form" status-icon>
                <el-form-item label="邮箱地址" prop="email">
                    <el-input v-model="form.email" />
                </el-form-item>
                <el-form-item>
                    <el-button type="success" @click="onSubmit(ruleFormRef)">
                        发送验证码
                    </el-button>
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
import { $resetPass } from '@/api/customer';
import { useEmailStore } from '@/stores/emailStore'

const ruleFormRef = ref()
const emailStore = useEmailStore()

const form = reactive({
    email: ''
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
    email: [
        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
        { validator: validate_email, message: '请输入正确的邮箱格式', trigger: ['blur'] }
    ],
})

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $resetPass(form.email)
                .then(function (data) {
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            // alert(form.email)
            emailStore.setEmail(form.email)
        } else {
            return false
        }
    })
}
</script>

<style scoped lang="scss">
.login {
    display: flex;
    align-items: center;
    height: 100vh;
    background-color: #c3cbd6;

    .left {
        width: 63%;
        height: 100vh;
        object-fit: cover;
    }
    
    .regPart {
            margin-left: auto;
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

::v-deep .el-form-item p{
    color:#303133;
    font-size: 20px;
}

::v-deep .el-button {
    min-height: 38px;
    height: 5vh;
    width: 30vh;
    min-width: 200px;
}

.login .box span,
.login .box p {
    display: flex;
    align-items: center;
}
</style>