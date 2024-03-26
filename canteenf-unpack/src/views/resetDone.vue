<template>
    <div class="login">
        <img class="left" src="../assets/img/resetDone_back.jpg" alt="left poster">
        <div class="box">
            <div class="logo-container">
                <img class="logo" src="../assets/img/logo.png" alt="left poster">
                <span class="logo-text">内部餐饮系统</span>
            </div>
            <div style="display: flex; text-align: center;">
                <p class="title">密码重置</p>
            </div>
            <el-form ref="ruleFormRef" :model="form" :rules="rules" label-width="20%" class="demo-form" status-icon>
                <el-form-item label="新密码" prop="password">
                    <el-input type="password" v-model="form.password" />
                </el-form-item>
                <el-form-item label="验证码" prop="v_code">
                    <el-input v-model="form.v_code" />
                </el-form-item>
                <el-form-item>
                    <el-button type="success" @click="onSubmit(ruleFormRef)">
                        重置密码
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
import { $resetDone } from '@/api/customer'
import { useEmailStore } from '@/stores/emailStore'

const ruleFormRef = ref()

const form = reactive({
    email: useEmailStore().getEmail,
    v_code: '',
    password: ''
})

const rules = reactive({
    v_code: [
        { required: true, message: '验证码不能为空', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '新密码不能为空', trigger: 'blur' },
    ]
})

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            console.log(form.password, form.v_code, form.email)
            $resetDone(form.password, form.v_code, form.email)
                .then(function (data) {
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
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