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
                    <el-menu default-active="4" class="el-menu-vertical-demo">
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
                                    <el-button type="success" @click="dialogVisible2 = true;">菜品上新</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="菜品名" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-card><br>
                <el-table :data="dishs" style="width: 100%">
                    <el-table-column prop="dish_name" label="菜品名" />
                    <el-table-column prop="dish_img" label="菜品图片">
                        <template #default="scope">
                            <el-image v-if="scope.row.dish_img" :src="scope.row.dish_img"
                                style="width: 80px; height: 80px;" fit="cover"></el-image>
                            <span v-else>暂无</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="dish_price" label="菜品价格" />
                    <el-table-column prop="dish_des" label="菜品描述" />
                    <el-table-column label="操作">
                        <template #default="scope">
                            <el-button type="info" size="small" @click="Detail(scope.row)">大图</el-button>
                            <el-button type="primary" size="small" @click="prepareEdit(scope.row)">编辑</el-button>
                            <el-button size="small" type="danger" @click="prepareDelete(scope.row)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <br>
                <div class="pagination-container">
                    <el-pagination v-model:current-page="currentPage1" :page-size="5" layout="prev, pager, next"
                        :total="total" @current-change="handleCurrentChange" />
                </div>
                <el-dialog style="margin-right: 54vh; margin-top: 40vh;" v-model="dialogVisible" title="操作确认"
                    width="500">
                    <span>此操作不可逆！是否确认删除菜品？</span>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="danger" @click="confirmDelete">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 54vh; margin-top: 20vh;" v-model="dialogVisible4" title="菜品大图"
                    width="500">
                    <br>
                    <el-image v-if="rowToEdit.dish_img" :src="rowToEdit.dish_img" style="width: 100%;"
                        fit="cover"></el-image>
                    <span v-else style="margin-left: 32%;">暂无图片，可修改后查看</span>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button type="info" @click="dialogVisible4 = false">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 54vh; margin-top: 30vh;" v-model="dialogVisible2" title="新建菜品"
                    width="500">
                    <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="菜品名" prop="dish_name">
                            <el-input v-model="form.dish_name" />
                        </el-form-item>
                        <el-form-item label="菜品价格" prop="dish_price">
                            <el-input v-model="form.dish_price" />
                        </el-form-item>
                        <el-form-item label="图片链接" prop="dish_img">
                            <el-input v-model="form.dish_img" />
                        </el-form-item>
                        <el-form-item label="菜品描述" prop="dish_des">
                            <el-input v-model="form.dish_des" />
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

                <el-dialog style="margin-right: 54vh; margin-top: 30vh;" v-model="dialogVisible3" title="菜品修改"
                    width="500">
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="菜品名" prop="dish_name">
                            <el-input v-model="form3.dish_name" />
                        </el-form-item>
                        <el-form-item label="菜品价格" prop="dish_price">
                            <el-input v-model="form3.dish_price" />
                        </el-form-item>
                        <el-form-item label="图片链接" prop="dish_img">
                            <el-input v-model="form3.dish_img" />
                        </el-form-item>
                        <el-form-item label="菜品描述" prop="dish_des">
                            <el-input v-model="form3.dish_des" />
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
import { $signout, $getDishData, $delDish, $addDish, $updateDish } from '@/api/shop';
import {
    Document, Avatar, DishDot,
    Setting, HomeFilled
} from '@element-plus/icons-vue'


const activeIndex = ref('1');
const username = useUserStore().getUsername
const router = useRouter();
const dishs = ref([]);
const currentPage1 = ref(1);
const rowToDelete = ref(null);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const dialogVisible4 = ref(false)
const total = ref(0);

const form2 = reactive({
    key: ''
})

const form = reactive({
    dish_name: '',
    dish_price: '',
    dish_des: '',
    dish_img: '',
})

const form3 = reactive({
    dish_name: '',
    dish_price: '',
    dish_des: '',
    dish_img: '',
})

const rule = reactive({
    dish_name: [
        { required: true, message: '菜品名称不能为空', trigger: 'blur' },
    ],
    dish_price: [
        { required: true, message: '菜品价格不能为空', trigger: 'blur' },
    ]
})

const getData = (key, pagenum) => {
    $getDishData(key, 5, pagenum, username)
        .then(function (response) {
            dishs.value = response.data.map(dish => {
                return dish;
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
            $addDish(username, form)
                .then(function (data) {
                    alert('菜品添加成功！')
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

function Detail(row) {
    rowToEdit.value = row;
    dialogVisible4.value = true;
}

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            let editedData = {
                dish_name: form3.dish_name,
                dish_price: form3.dish_price,
                dish_des: form3.dish_des,
                dish_img: form3.dish_img
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
    $updateDish(id, editedRow)
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
    $delDish(rows.id)
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