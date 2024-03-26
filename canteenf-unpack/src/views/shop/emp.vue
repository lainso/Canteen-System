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
                    <el-menu default-active="3" class="el-menu-vertical-demo">
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
            <el-main style="background-image: none; display: block; height: auto;">
                <el-card class="box-card" shadow="hover">
                    <div class="form-wrapper">
                        <div class="new-button-container">
                            <el-form :inline="true" label-width="20%">
                                <el-form-item class="add-button-item">
                                    <el-button type="success" @click="dialogVisible2 = true;">添加雇员</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="员工名称" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-card><br>
                <el-table :data="emps" style="width: 100%">
                    <el-table-column prop="emp_name" label="员工名称" />
                    <el-table-column prop="emp_role" label="员工职位" />
                    <el-table-column prop="emp_number" label="员工编号" />
                    <el-table-column prop="emp_tel" label="联系电话" />
                    <el-table-column prop="emp_condition" label="员工状态" />
                    <el-table-column label="操作">
                        <template #default="scope">
                            <el-button type="primary" size="small" @click="prepareEdit(scope.row)">编辑</el-button>
                            <el-button size="small" type="danger" @click="prepareDelete(scope.row)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <br>
                <div class="pagination-container">
                    <el-pagination v-model:current-page="currentPage1" :page-size="11" layout="prev, pager, next"
                        :total="total" @current-change="handleCurrentChange" />
                </div>
                <el-dialog style="margin-right: 54vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                    width="500">
                    <span>此操作不可逆！是否确认删除员工？</span>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="danger" @click="confirmDelete">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 54vh; margin-top: 30vh;" v-model="dialogVisible2" title="添加员工"
                    width="500">
                    <p>* 可前往 👉<a href="/#/shop/me">个人中心</a>👈 获取邀请链接和邀请码，快速完成添加。</p><br>
                    <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="员工名称" prop="emp_name">
                            <el-input v-model="form.emp_name" />
                        </el-form-item>
                        <el-form-item label="员工职位" prop="emp_role">
                            <el-input v-model="form.emp_role" />
                        </el-form-item>
                        <el-form-item label="员工编号" prop="emp_number">
                            <el-input v-model="form.emp_number" />
                        </el-form-item>
                        <el-form-item label="联系电话" prop="emp_tel">
                            <el-input v-model="form.emp_tel" />
                        </el-form-item>
                        <el-form-item label="员工状态" prop="emp_condition">
                            <el-input v-model="form.emp_condition" />
                        </el-form-item>
                    </el-form>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                            <el-button type="success" @click="createCus(ruleFormRef)">
                                提交
                            </el-button>
                        </div>
                    </template>
                </el-dialog>

                <el-dialog style="margin-right: 54vh; margin-top: 30vh;" v-model="dialogVisible3" title="修改员工信息"
                    width="500">
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="员工名称" prop="emp_name">
                            <el-input v-model="form3.emp_name" />
                        </el-form-item>
                        <el-form-item label="员工职位" prop="emp_role">
                            <el-input v-model="form3.emp_role" />
                        </el-form-item>
                        <el-form-item label="员工编号" prop="emp_number">
                            <el-input v-model="form3.emp_number" />
                        </el-form-item>
                        <el-form-item label="联系电话" prop="emp_tel">
                            <el-input v-model="form3.emp_tel" />
                        </el-form-item>
                        <el-form-item label="员工状态" prop="emp_condition">
                            <el-input v-model="form3.emp_condition" />
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
import { useUserStore } from '@/stores/userStore'
import { $signout, $getEmpData, $delEmp, $addEmp, $updateEmp } from '@/api/shop';
import {
    Document, Avatar, DishDot,
    Setting, HomeFilled
} from '@element-plus/icons-vue'


const activeIndex = ref('1');
const username = useUserStore().getUsername
const router = useRouter();
const emps = ref([]);
const currentPage1 = ref(1);
const rowToDelete = ref(null);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const total = ref(0);

const form2 = reactive({
    key: ''
})

const form = reactive({
    emp_name: '',
    emp_number: '',
    emp_role: '',
    emp_tel: '',
    emp_condition: '',
})

const form3 = reactive({
    emp_name: '',
    emp_number: '',
    emp_role: '',
    emp_tel: '',
    emp_condition: '',
})

const rule = reactive({
    emp_name: [
        { required: true, message: '员工名称不能为空', trigger: 'blur' },
    ],
    emp_number: [
        { required: true, message: '员工编号不能为空', trigger: 'blur' },
    ],
    emp_role: [
        { required: true, message: '员工角色不能为空', trigger: 'blur' },
    ],
    emp_tel: [
        { required: true, message: '员工电话不能为空', trigger: 'blur' },
    ],
    emp_condition: [
        { required: true, message: '员工状态不能为空', trigger: 'blur' },
    ]
})

const getData = (key, pagenum) => {
    $getEmpData(key, 11, pagenum, username)
        .then(function (response) {
            emps.value = response.data.map(emp => {
                return emp;
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
            $addEmp(username, form)
                .then(function (data) {
                    alert('员工添加成功！')
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
        form3[key] = row[key] ?? "";
    });
    console.log(form3, row)
    dialogVisible3.value = true;
}

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            let editedData = {
                emp_name: form3.emp_name,
                emp_number: form3.emp_number,
                emp_tel: form3.emp_tel,
                emp_condition: form3.emp_condition,
                emp_role: form3.emp_role,
            };
            const id = rowToEdit.value.id;
            editCus(id, editedData);
            dialogVisible3.value = false;
        } else {
            console.log("编辑表单验证失败");
        }
    });
}

const editCus = (id, editedRow) => {
    $updateEmp(id, editedRow)
        .then(function (data) {
            alert('修改成功！')
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
    $delEmp(rows.id)
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

onMounted(() => {
    getData('', 1);
});

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