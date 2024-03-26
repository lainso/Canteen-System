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
                    <el-menu default-active="2" class="el-menu-vertical-demo">
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
                                    <el-button type="success" @click="dialogVisible2 = true;">新增账户</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="账户名" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                    <h6 style="margin-left: 63vh; margin-top: 7px; color: red;">* 管理员账户不会被显示</h6>
                </el-card><br>
                <el-table :data="customers" style="width: 100%">
                    <el-table-column prop="username" label="账户名" />
                    <el-table-column prop="first_name" label="昵称" width="120"/>
                    <el-table-column prop="email" label="电子邮件" width="250"/>
                    <el-table-column prop="cus_tel" label="联系电话" />
                    <el-table-column prop="usertype" label="账户类型" />
                    <el-table-column prop="last_login" label="上次登录时间" />
                    <el-table-column label="操作" width="280">
                        <template #default="scope">
                            <el-button type="info" size="small" @click="Detail(scope.row)">详情</el-button>
                            <el-button type="primary" size="small" @click="prepareEdit(scope.row)">编辑</el-button>

                            <el-button v-if="scope.row.usertype === '商户'" size="small" type="warning" @click="prepareReset(scope.row)">改密</el-button>
                            <el-tooltip class="box-item" effect="dark" content="请修改正确邮箱后让用户自行重置"
                                v-if="scope.row.usertype === '顾客'" placement="top-end">
                                <el-button :disabled="scope.row.usertype === '顾客'" size="small" type="warning">改密</el-button>
                            </el-tooltip>

                            <el-button v-if="scope.row.usertype === '顾客'" size="small" type="danger" @click="prepareDelete(scope.row)">删除</el-button>
                            <el-tooltip class="box-item" effect="dark" content="删除商户请前往：商户管理-商户"
                                v-if="scope.row.usertype === '商户'" placement="top-end">
                                <el-button :disabled="scope.row.usertype === '商户'" size="small" type="danger">删除</el-button>
                            </el-tooltip>
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
                    <span>此操作不可逆！是否确认删除该账户？</span>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="danger" @click="confirmDelete">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 56vh; margin-top: 15vh;" v-model="dialogVisible4" title="账户详情"
                    width="500">
                    <br>
                    <p><span class="label">账户名：</span>{{ rowToEdit.username }}</p><br>
                    <p><span class="label">昵称：</span>{{ rowToEdit.first_name }}</p><br>
                    <p><span class="label">联系电话：</span>{{ rowToEdit.cus_tel }}</p><br>
                    <p><span class="label">电子邮件：</span>{{ rowToEdit.email }}</p><br>

                    <p><span class="label">性别：</span>{{ rowToEdit.cus_sex }}</p><br>
                    <p><span class="label">生日：</span>{{ fixTime(rowToEdit.cus_birth) }}</p><br>
                    <p><span class="label">地址：</span>{{ rowToEdit.cus_address }}</p><br>
                    <p><span class="label">账户类型：</span>{{ rowToEdit.usertype }}</p><br>
                    <p><span class="label">是否激活：</span>{{ rowToEdit.is_active ? '是' : '否' }}</p><br>
                    <p><span class="label">上次登录：</span>{{ fixTime(rowToEdit.last_login) }}</p><br>
                    <p><span class="label">注册时间：</span>{{ fixTime(rowToEdit.date_joined) }}</p><br>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button type="info" @click="dialogVisible4 = false">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 58vh; margin-top: 8vh;" v-model="dialogVisible2" title="新建账户"
                    width="500">
                    <p style="font-size: 13px;">* 若需要创建商户账号，请前往 👉<a href="#/super/shop">商户管理-商户</a>👈 创建。</p><br>
                    <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="账户名" prop="username">
                            <el-input v-model="form.username" placeholder="创建后不可更改" />
                        </el-form-item>
                        <el-form-item label="昵称" prop="first_name">
                            <el-input v-model="form.first_name" />
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="form.password" />
                        </el-form-item>
                        <el-form-item label="电子邮件" prop="email">
                            <el-input v-model="form.email" placeholder="账户需要接收邮件以修改密码等" />
                        </el-form-item>
                        <el-form-item label="账户类型" prop="usertype">
                            <el-select v-model="form.usertype">
                                <el-option label="客户" value="customer" />
                                <el-option label="管理员" value="super" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="是否激活" prop="is_active">
                            <el-select v-model="form.is_active">
                                <el-option label="是" value="1" />
                                <el-option label="否" value="0" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="联系电话" prop="cus_tel">
                            <el-input v-model="form.cus_tel" />
                        </el-form-item>
                        <el-form-item label="性别" prop="cus_sex">
                            <el-select v-model="form.cus_sex">
                                <el-option label="男" value="男" />
                                <el-option label="女" value="女" />
                                <el-option label="保密" value="保密" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="生日" prop="cus_birth">
                            <el-date-picker v-model="form.cus_birth" type="date" clearable />
                        </el-form-item>
                        <el-form-item label="地址" prop="cus_address">
                            <el-input v-model="form.cus_address" />
                        </el-form-item>

                    </el-form>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                            <el-button type="success" @click="createCus(ruleFormRef)">
                                确认新增
                            </el-button>
                        </div>
                    </template>
                </el-dialog>

                <el-dialog style="margin-right: 58vh; margin-top: 15vh;" v-model="dialogVisible3" title="账户修改"
                    width="500">

                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="昵称" prop="first_name">
                            <el-input v-model="form3.first_name" />
                        </el-form-item>
                        <el-form-item label="电子邮件" prop="email">
                            <el-input v-model="form3.email" />
                        </el-form-item>
                        <el-form-item label="账户类型" prop="usertype">
                            <el-select v-model="form3.usertype">
                                <el-option label="客户" value="customer" />
                                <el-option label="商家" value="shop" />
                                <el-option label="管理员" value="super" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="是否激活" prop="is_active">
                            <el-select v-model="form3.is_active">
                                <el-option label="是" value="True" />
                                <el-option label="否" value="False" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="联系电话" prop="cus_tel">
                            <el-input v-model="form3.cus_tel" />
                        </el-form-item>
                        <el-form-item label="性别" prop="cus_sex">
                            <el-select v-model="form3.cus_sex">
                                <el-option label="男" value="男" />
                                <el-option label="女" value="女" />
                                <el-option label="保密" value="保密" />
                            </el-select>
                        </el-form-item>
                        <el-form-item label="生日" prop="cus_birth">
                            <el-date-picker v-model="form3.cus_birth" type="date" clearable />
                        </el-form-item>
                        <el-form-item label="地址" prop="cus_address">
                            <el-input v-model="form3.cus_address" />
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
                <el-dialog style="margin-right: 56vh; margin-top: 40vh;" v-model="dialogVisible5" title="操作确认"
                    width="500">
                    <span>此操作不可逆！是否确认重置商户密码？</span>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="warning" @click="confirmReset">
                                确认
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
import { $signout, $getCusData, $delCus, $addCus, $updateCus, $resetShopPass } from '@/api/super';
import {
    Document, Avatar, ForkSpoon,
    ChatDotSquare, DocumentChecked,
    CreditCard,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const customers = ref([]);
const currentPage1 = ref(1);
const rowToDelete = ref(null);
const rowToReset = ref(null);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const dialogVisible4 = ref(false)
const dialogVisible5 = ref(false)
const total = ref(0);

const form2 = reactive({
    key: ''
})

const form = reactive({
    username: '',
    first_name: '',
    password: '',
    email: '',
    usertype: '',
    is_active: '',
    cus_tel: '',
    cus_sex: '',
    cus_birth: '',
    cus_address: ''
})

const form3 = reactive({
    first_name: '',
    password: '',
    email: '',
    usertype: '',
    is_active: '',
    cus_tel: '',
    cus_sex: '',
    cus_birth: '',
    cus_address: ''
})

const prepareReset = (row) => {
    rowToReset.value = row;
    dialogVisible5.value = true;
}

function confirmReset() {
    if (rowToReset.value) {
        handleReset(rowToReset.value);
    }
    dialogVisible5.value = false;
}

const handleReset = (rows) => {
    $resetShopPass(rows.username)
        .then(function (info) {
            alert(info);
            getData('', 1);
        })
        .catch(function (error) {
            console.log(error);
        });
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

const rule = reactive({
    username: [
        { required: true, message: '账户名不能为空', trigger: 'blur' },
    ],
    password: [
        { required: true, message: '密码不能为空', trigger: 'blur' },
    ],
    first_name: [
        { required: true, message: '昵称不能为空', trigger: 'blur' },
    ],
    email: [
        { required: true, message: '电子邮箱不能为空', trigger: 'blur' },
        { validator: validate_email, message: '请输入正确的邮箱格式', trigger: ['blur'] }
    ],
    usertype: [
        { required: true, message: '请选择账户类型', trigger: 'blur' },
    ],
    is_active: [
        { required: true, message: '请选择用户激活状态', trigger: 'blur' },
    ],
})

const userTypeMappings = {
    super: "管理员",
    shop: "商户",
    customer: "顾客"
};

const fixUserType = (usertype) => {
    return userTypeMappings[usertype] || usertype;
};

const getData = (key, pagenum) => {
    $getCusData(key, 11, pagenum)
        .then(function (response) {
            customers.value = response.data.map(customer => {
                customer.last_login = fixTime(customer.last_login);
                customer.usertype = fixUserType(customer.usertype);
                customer.is_active = customer.is_active ? '是' : '否';
                return customer;
            });
            total.value = response.total;
        })
        .catch(function (error) {
            console.log(error);
        });
}

const search = (key) => {
    getData(key, 1);
}

const createCus = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            console.log(form)
            $addCus(form)
                .then(function (data) {
                    alert('账户添加成功！')
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
    rowToEdit.value = JSON.parse(JSON.stringify(row));
    Object.keys(form3).forEach(key => {
        if (key === 'is_active') {
            form3[key] = row[key] === '是' ? 'True' : 'False';
        } else {
            form3[key] = row[key] ?? "";
        }
    });
    dialogVisible3.value = true;
}

function Detail(row) {
    rowToEdit.value = row;
    dialogVisible4.value = true;
}

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            if(form3.usertype === '商户'){
                form3.usertype = 'shop';
            } else if (form3.usertype === '管理员'){
                form3.usertype = 'super';
            }else{
                form3.usertype = 'customer';
            }
            let editedData = {
                email: form3.email,
                fname: form3.first_name,
                sex: form3.cus_sex,
                tel: form3.cus_tel,
                birth: form3.cus_birth,
                address: form3.cus_address,
                is_active: form3.is_active,
                usertype: form3.usertype
            };
            const cusID = rowToEdit.value.id;
            editCus(cusID, editedData);
            dialogVisible3.value = false;
        } else {
            console.log("编辑表单验证失败");
        }
    });
}

const editCus = (cusID, editedRow) => {
    $updateCus(cusID, editedRow)
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
    $delCus(rows.id)
        .then(function (info) {
            alert(info);
            getData('', 1);
        })
        .catch(function (error) {
            console.log(error);
        });
}

const handleCurrentChange = (val) => {
    getData(form2.key, val)
}


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

.label {
    font-weight: bold;
    display: inline-block;
    min-width: 5rem;
    text-align: right;
    margin-right: .5rem;
}
</style>