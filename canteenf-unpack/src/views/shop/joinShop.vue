<template>
    <div class="login">
        <img class="left" src="../../assets/img/shop/joinShop_back.jpg" alt="left poster">
        <div class="box">
            <div class="logo-container">
                <img class="logo" src="../../assets/img/logo.png" alt="left poster">
                <span class="logo-text">内部餐饮系统</span>
            </div>
            <div style="display: flex; text-align: center;">
                <p class="title">加入商户</p>
            </div>
            <el-form ref="ruleFormRef" :model="form" :rules="rules" label-width="20%" class="demo-form" status-icon>
                <el-form-item label="姓名" prop="emp_name">
                    <el-input v-model="form.emp_name" />
                </el-form-item>
                <el-form-item label="联系电话" prop="emp_tel">
                    <el-input v-model="form.emp_tel" />
                </el-form-item>
                <el-form-item label="邀请码" prop="shop_pass">
                    <el-input v-model="form.shop_pass" />
                </el-form-item>
                <el-form-item>
                    <el-button type="success" @click="onSubmit(ruleFormRef)">
                        加入
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
import { $joinShop } from '@/api/shop';
import { useRouter } from 'vue-router';
const ruleFormRef = ref()
const router = useRouter();

const form = reactive({
    emp_name: '',
    emp_tel: '',
    shop_pass: ''
})

const rules = reactive({
    emp_name: [
        { required: true, message: '您的姓名不能为空', trigger: 'blur' },
    ],
    emp_tel: [
        { required: true, message: '您的联系方式不能为空', trigger: 'blur' },
    ],
    shop_pass: [
        { required: true, message: '邀请码不能为空', trigger: 'blur' },
    ],
})

const onSubmit = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $joinShop(form)
                .then(function (data) {
                    alert('加入成功！')
                    router.push('/')
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
    background-color: #c3cbd6;

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