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
                    <el-menu default-active="3" class="el-menu-vertical-demo">
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
            <el-main style="background-image: none; display: block; height: auto;">
                <el-card class="box-card" shadow="hover">
                    <div class="form-wrapper">
                        <!-- "新增"按钮容器 -->
                        <div class="new-button-container">
                            <el-form :inline="true" label-width="20%">
                                <el-form-item class="add-button-item">
                                    <el-button type="success" @click="dialogVisible2 = true;">创建商户</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="商户名称" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-card><br>
                <el-table :data="shops" style="width: 100%">
                    <el-table-column prop="shop_name" label="商户名称" width="120" />
                    <el-table-column prop="shop_number" label="商户编号" />
                    <el-table-column prop="shop_cus" label="登录账户" />
                    <el-table-column prop="shop_tel" label="联系电话" />
                    <el-table-column prop="shop_head" label="店长名称" />
                    <el-table-column prop="shop_pass" label="邀请码" />
                    <el-table-column label="操作">

                        <template #default="scope">
                            <el-button type="primary" size="small"
                                @click="prepareEdit(scope.row)">编辑</el-button>
                            <el-button size="small" type="danger" @click="prepareDelete(scope.row)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <br>
                <div class="pagination-container">
                    <el-pagination v-model:current-page="currentPage1" :page-size="11" layout="prev, pager, next"
                        :total="total" @current-change="handleCurrentChange" />
                </div>
                <el-dialog style="margin-right: 56vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                    width="500">
                    <span>此操作不可逆！是否确认删除该商户？</span>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="danger" @click="confirmDelete">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 58vh; margin-top: 10vh;" v-model="dialogVisible2" title="新建商户"
                    width="500">
                    <br>
                    <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="20%" class="demo-form"
                        status-icon>
                        <el-form-item label="商户名称" prop="shop_name">
                            <el-input v-model="form.shop_name" />
                        </el-form-item>
                        <el-form-item label="登录账号" prop="username">
                            <el-input v-model="form.username" />
                        </el-form-item>
                        <el-form-item label="登陆密码" prop="password">
                            <el-input v-model="form.password" type="password" />
                        </el-form-item>
                        <el-form-item label="是否激活" prop="is_active">
                            <el-select v-model="form.is_active">
                                <el-option label="是" value="1" />
                                <el-option label="否" value="0" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="联系电话" prop="shop_tel">
                            <el-input v-model="form.shop_tel" />
                        </el-form-item>
                        <el-form-item label="邀请码" prop="shop_pass">
                            <el-input v-model="form.shop_pass" placeholder="用于店铺快速添加新雇员" />
                        </el-form-item>
                        <el-form-item label="电子邮件" prop="email">
                            <el-input v-model="form.email" />
                        </el-form-item>
                        <el-form-item label="店长名称" prop="shop_head">
                            <el-input v-model="form.shop_head" />
                        </el-form-item>
                        <el-form-item label="店铺地址" prop="cus_address">
                            <el-input v-model="form.address" />
                        </el-form-item>
                    </el-form>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                            <el-button type="success" @click="createShop(ruleFormRef)">
                                确认创建
                            </el-button>
                        </div>
                    </template>
                </el-dialog>

                <el-dialog style="margin-right: 58vh; margin-top: 25vh;" v-model="dialogVisible3" title="商户信息修改"
                    width="500">
                    <br>
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="商户名称" prop="shop_name">
                            <el-input v-model="form3.shop_name" />
                        </el-form-item>
                        <el-form-item label="联系电话" prop="shop_tel">
                            <el-input v-model="form3.shop_tel" />
                        </el-form-item>
                        <el-form-item label="邀请码" prop="shop_pass">
                            <el-input v-model="form3.shop_pass" />
                        </el-form-item>
                        <el-form-item label="店长名称" prop="shop_head">
                            <el-input v-model="form3.shop_head" />
                        </el-form-item>
                    </el-form>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible3 = false; onReset2(ruleFormRef)">取消</el-button>
                            <el-button type="primary" @click="confirmEdit">
                                确认修改
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { $signout, $getShopData, $delShop, $addShop, $updateShop } from '@/api/super';
import {
    Document, Avatar, ForkSpoon,
    ChatDotSquare, DocumentChecked,
    CreditCard,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const shops = ref([]);
const currentPage1 = ref(1);
const rowToDelete = ref(null);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const total = ref(0);

const form = reactive({
    username: '',
    password: '',
    email: '',
    address: '',
    is_active: '',
    shop_name: '',
    shop_cus: '',
    shop_tel: '',
    shop_head: '',
    shop_pass: '',
})

const form2 = reactive({
    key: ''
})

const form3 = reactive({
    shop_name: '',
    shop_tel: '',
    shop_head: '',
    shop_pass: '',
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

const rule = reactive({
    shop_name: [
        { required: true, message: '商户名称不能为空', trigger: 'blur' },
    ],
    shop_tel: [
        { required: true, message: '商户联系电话不能为空', trigger: 'blur' },
    ],
    shop_pass: [
        { required: true, message: '商户邀请码不能为空', trigger: 'blur' },
    ],
    shop_cus: [
        { required: true, message: '商户绑定账号不能为空', trigger: 'blur' },
    ],
    username: [
        { required: true, message: '账户名不能为空', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '密码不能为空', trigger: 'blur' },
    ],
    email: [
        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
        { validator: validate_email, message: '请输入正确的邮箱格式', trigger: ['blur'] }
    ],
    is_active: [
        { required: true, message: '请选择用户激活状态', trigger: 'blur' },
    ],
})

const getData = (key, pagenum) => {
    $getShopData(key, 11, pagenum)
        .then(function (response) {
            shops.value = response.data.map(promo => {
                return promo;
            });
            total.value = response.total;
        })
        .catch(function (error) {
            console.log(error);
        });
}

const createShop = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            console.log(form)
            $addShop(form)
                .then(function (data) {
                    alert('新增商户成功！')
                    onReset()
                    dialogVisible2.value = false;
                    getData('', 1);
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

function prepareEdit(row) {
    rowToEdit.value = row;
    Object.keys(form3).forEach(key => {
        form3[key] = row[key] ?? "";
    });
    dialogVisible3.value = true;
}

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            let editedData = {
                shop_name: form3.shop_name,
                shop_head: form3.shop_head,
                shop_tel: form3.shop_tel,
                shop_pass: form3.shop_pass,
            };
            const id = rowToEdit.value.id;
            editShop(id, editedData);
            dialogVisible3.value = false;
        } else {
            console.log("编辑表单验证失败");
        }
    });
}

const editShop = (id, editedRow) => {
    console.log(id, editedRow);
    $updateShop(id, editedRow)
        .then(function (data) {
            alert('修改成功')
            console.log(data);
            getData('', 1);
        })
        .catch(function (error) {
            console.log(error);
        });
    onReset2();
}

function prepareDelete(row) {
    rowToDelete.value = row;
    dialogVisible.value = true;
}

function confirmDelete() {
    if (rowToDelete.value) {
        handleDelete(rowToDelete.value);
    }
    dialogVisible.value = false;
}

const handleDelete = (rows) => {
    $delShop(rows.id)
        .then(function (info) {
            alert('删除成功！')
            getData('', 1);
        })
        .catch(function (error) {
            console.log(error);
        });
}

const search = (key) => {
    getData(key, 1);
}

const handleCurrentChange = (val) => {
    getData(form2.key, val)
}

const onReset = () => {
    if (ruleFormRef.value) {
        ruleFormRef.value.resetFields();
    }
}

const onReset2 = () => {
    if (ruleFormRef3.value) {
        ruleFormRef3.value.resetFields();
    }
}

onMounted(() => {
    getData('', 1);
});

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

.flex-grow {
    flex-grow: 1;
}

el-container {
    height: calc(100vh - 84px);
}

.form-wrapper {
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

.new-button-container {
    display: flex;
    align-items: center;
}

.search-area {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
    max-width: 85%;
}

.demo-form-inline.search-form {
    justify-content: center;
}

.add-button-item,
.search-form .el-form-item {
    margin-bottom: 0;
    margin-right: 2 0px;
}

.pagination-container {
    position: fixed;
    bottom: 4%;
    left: 50%;
    width: 100%;
    z-index: 1000;
}

::v-deep .el-date-editor {
    width: 100%;
}
</style>