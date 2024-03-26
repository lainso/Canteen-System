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
                    <el-menu default-active="2" class="el-menu-vertical-demo">
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
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="订单时间" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable
                                        placeholder="例：2024-01-01" />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-card><br>
                <el-table :data="orders" style="width: 100%" :row-class-name="tableRowClassName">
                    <el-table-column prop="ord_time" label="订单时间" width="180" />
                    <el-table-column prop="username" label="顾客账号" width="150" />
                    <el-table-column prop="ord_condition" label="订单状态" width="150" />
                    <el-table-column prop="ord_money" label="订单金额" width="150" />
                    <el-table-column label="订单内容">
                        <template #default="scope">
                            {{ formatOrderList(scope.row.orderlist) }}
                        </template>
                    </el-table-column>
                    <el-table-column prop="ord_number" label="订单号" width="180" />
                    <el-table-column label="操作" width="150">
                        <template #default="scope">
                            <el-button type="primary" size="small" @click="prepareEdit(scope.row)">编辑</el-button>
                            <el-tooltip class="box-item" effect="dark" content="商户禁止删除订单，可前往编辑修改订单状态"
                                placement="top-end">
                                <el-button disabled size="small" type="danger">删除</el-button>
                            </el-tooltip>
                        </template>
                    </el-table-column>
                </el-table>
                <br>
                <div class="pagination-container">
                    <el-pagination v-model:current-page="currentPage1" :page-size="7" layout="prev, pager, next"
                        :total="total" @current-change="handleCurrentChange" />
                </div>
                <el-dialog style="margin-right: 58vh; margin-top: 35vh;" v-model="dialogVisible3" title="修改订单状态"
                    width="500">
                    <p>商户只可以修改订单状态。</p><br>
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="订单状态" prop="ord_condition">
                            <el-select v-model="form3.ord_condition">
                                <el-option label="未支付" value="未支付" />
                                <el-option style="color: orange;" label="已支付" value="已支付" />
                                <el-option style="color: green;" label="已完成" value="已完成" />
                                <el-option style="color: red;" label="已取消" value="已取消" />
                            </el-select>
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
import { $signout, $getOrderData, $updateOrder } from '@/api/shop';
import {
    Document, Avatar, DishDot,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const orders = ref([]);
const user = useUserStore().getUsername
const currentPage1 = ref(1);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible3 = ref(false)
const total = ref(0);

const tableRowClassName = ({ row, rowIndex }) => {
    if (row.ord_condition === '已支付') {
        return 'warning-row';
    } else if (row.ord_condition === '已完成') {
        return 'success-row';
    } else if (row.ord_condition === '已取消') {
        return 'danger-row';
    }
    return '';
};

const form2 = reactive({
    key: ''
})

const form3 = reactive({
    ord_condition: ''
})

const rule = reactive({
    ord_condition: [
        { required: true, message: '订单状态不能为空', trigger: 'blur' },
    ]
})

const getData = (key, pagenum) => {
    $getOrderData(key, 7, pagenum, user)
        .then(function (response) {
            orders.value = response.data.map(order => {
                return order;
            });
            total.value = response.total;
        })
        .catch(function (error) {
            console.log(error);
        });
}

const formatOrderList = (orderList) => {
    return orderList.map(item => `${item.dish_name} × ${item.orderlist_num}`).join('，');
}

onMounted(() => {
    getData('', 1);
});

const search = (key) => {
    getData(key, 1);
}

function prepareEdit(row) {
    rowToEdit.value = row;
    dialogVisible3.value = true;
}

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            let editedData = {
                ord_condition: form3.ord_condition
            };
            const ord_num = rowToEdit.value.ord_number;
            editOrder(ord_num, editedData);
            dialogVisible3.value = false;
        } else {
            console.log("编辑表单验证失败");
        }
    });
}

const editOrder = (ord_num, editedRow) => {
    $updateOrder(ord_num, editedRow)
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

const handleCurrentChange = (val) => {
    getData(form2.key, val)
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

const onReset2 = () => {
    if (ruleFormRef3.value) {
        ruleFormRef3.value.resetFields();
    }
}
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
    max-width: 100%;
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

::v-deep .warning-row {
    --el-table-tr-bg-color: var(--el-color-warning-light-9);
}

::v-deep .danger-row {
    --el-table-tr-bg-color: var(--el-color-danger-light-9);
}

::v-deep .success-row {
    --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>