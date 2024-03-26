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
            <el-main style="background-image: none;">
                <el-row>
                    <el-col class="col2" :span="15">
                        <el-card class="box-card" shadow="hover" style="width: 100%;">
                            <el-form :inline="true" :model="form2" label-width="50%" style="margin-left: 21%;"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="菜品名" prop="key" label-width="20%">
                                    <el-input v-model="form2.key" style="width: 300px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </el-card><br>
                        <el-table :data="dishs">
                            <el-table-column prop="dish_name" label="菜品名" />
                            <el-table-column prop="dish_img" label="菜品图片">
                                <template #default="scope">
                                    <el-image v-if="scope.row.dish_img" :src="scope.row.dish_img"
                                        style="width: 80px; height: 80px;" fit="cover"></el-image>
                                    <span v-else>暂无</span>
                                </template>
                            </el-table-column>
                            <el-table-column prop="dish_price" label="菜品价格" />
                            <el-table-column label="操作">
                                <template #default="scope">
                                    <el-button type="primary" size="small" @click="Detail(scope.row)">大图</el-button>
                                    <el-button type="success" size="small" @click="addDish(scope.row)">添加</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <br>
                        <div class="pagination-container">
                            <el-pagination v-model:current-page="currentPage1" :page-size="5" layout="prev, pager, next"
                                :total="total" @current-change="handleCurrentChange" />
                        </div>
                    </el-col>
                    <el-col :span="1"></el-col>
                    <el-col :span="8">
                        <!-- 订单区域 -->
                        <el-card class="box-card" shadow="hover">
                            <p style="text-align: center; font-size: 30px;">新 订 单</p><br>
                            <el-table :data="orderList">
                                <el-table-column prop="dish_name" label="菜品名" />
                                <el-table-column prop="dish_price" label="单价" />
                                <el-table-column prop="count" label="数量" />
                                <el-table-column label="操作" width="100">
                                    <template #default="scope">
                                        <el-button size="small" type="success" :icon="Plus" circle
                                            @click="addOrderItem(scope.$index)" />
                                        <el-button size="small" type="danger" :icon="Minus" circle
                                            @click="removeOrderItem(scope.$index)" />
                                    </template>
                                </el-table-column>
                            </el-table><br>
                            <div class="button-container" style="text-align: right;">
                                <span style="margin-right: 20px;">总价：{{ OrderPrice }}</span>
                                <el-button type="primary" @click="prepareSubmit">提交订单</el-button>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <el-dialog style="margin-left: 40vh; margin-top: 18vh;" v-model="dialogVisible4" title="菜品大图"
                    width="500">
                    <br>
                    <el-image v-if="rowToSubmit.dish_img" :src="rowToSubmit.dish_img" style="width: 100%; height: 100%;"
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

                <el-dialog style="margin-right: 65vh; margin-top: 25vh;" v-model="dialogVisible3" title="订单结算"
                    width="500">
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <span style="margin-left: 2.5%;">订单详情：</span>
                        <template v-for="item in orderList" :key="item.dish_id">
                            <span>{{ item.dish_name }} x {{ item.count }}，</span>
                        </template><br><br>
                        <h2 style="font-weight: bold; text-align: right;">总价：{{ OrderPrice }}</h2><br>
                        <el-form-item label="客户账号" prop="username">
                            <el-input v-model="form3.username" />
                        </el-form-item>
                        <el-form-item label="结算方式" prop="pay_way">
                            <el-select v-model="form3.pay_way">
                                <el-option label="支付卡" value="支付卡" />
                                <el-option label="移动支付" value="移动支付" />
                                <el-option style="color: red;" label="稍后支付（ 挂起订单 ）" value="挂起订单" />
                            </el-select>
                        </el-form-item>
                    </el-form>
                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible3 = false; onReset2(ruleFormRef3)">取消</el-button>
                            <el-button type="primary" @click="confirmSubmit">
                                结算
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
import { $signout, $getDishData, $addOrder, $addPayment, $updatePaycard } from '@/api/shop';
import {
    Document, Avatar, DishDot,
    Setting, HomeFilled, Minus, Plus
} from '@element-plus/icons-vue'


const activeIndex = ref('1');
const username = useUserStore().getUsername
const router = useRouter();
const dishs = ref([]);
const ruleFormRef3 = ref(null);
const currentPage1 = ref(1);
const rowToSubmit = ref(null);
const user = useUserStore().getUsername
const dialogVisible3 = ref(false)
const dialogVisible4 = ref(false)
const total = ref(0);
const OrderPrice = ref(0);
const orderList = ref([]);
const form2 = reactive({
    key: ''
})

const form3 = reactive({
    username: '',
    pay_way: ''
})

const rule = reactive({
    username: [
        { required: true, message: '用户账户不能为空', trigger: 'blur' },
    ],
    pay_way: [
        { required: true, message: '请选择订单支付方式', trigger: 'blur' },
    ]
})

function prepareSubmit(row) {
    if (orderList.value.length === 0) {
        alert('请先添加菜品到订单中！');
    } else {
        rowToSubmit.value = JSON.parse(JSON.stringify(row));
        dialogVisible3.value = true;
    }

}

function confirmSubmit() {
    if (!ruleFormRef3.value || !rowToSubmit.value) return;
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            let editedData = {
                username: form3.username,
                pay_way: form3.pay_way,
                ord_list: JSON.stringify(orderList.value),
                money: OrderPrice.value,
                user: user,
                ord_condition: '',
                ord_id: ''
            };
            postAddOrder(editedData);
            dialogVisible3.value = false;
        } else {
            console.error("提交表单验证失败");
        }
    });
}

const postAddOrder = (data) => {
    if (data.pay_way === '挂起订单') {
        data.ord_condition = '未支付'
        $addOrder(data)
            .then(function (info) {
                console.log(info);
                alert('订单创建成功，顾客支付后请手动前往订单管理修改订单状态！')
                orderList.value = [];
                OrderPrice.value = 0;
            })
            .catch(function (error) {
                console.log(error);
            });
    } else if (data.pay_way === '支付卡') {
        data.ord_condition = '已支付'
        $addOrder(data)
            .then(function (response) {
                data.ord_id = response.id
                $addPayment(data)
                    .then(function (response) {
                        $updatePaycard(data)
                            .then(function (response) {
                                console.log(response);
                                alert('订单创建成功！')
                                orderList.value = [];
                                OrderPrice.value = 0;
                            })
                            .catch(function (error) {
                                console.log(error);
                            });
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            })
            .catch(function (error) {
                console.log(error);
            });
    } else {
        data.ord_condition = '已支付'
        $addOrder(data)
            .then(function (response) {
                data.ord_id = response.id
                $addPayment(data)
                    .then(function (response) {
                        console.log(response);
                        alert('订单创建成功！')
                        orderList.value = [];
                        OrderPrice.value = 0;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            })
            .catch(function (error) {
                console.log(error);
            });
    }
}

const onReset2 = () => {
    if (ruleFormRef3.value) {
        ruleFormRef3.value.resetFields();
    }
}

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

function Detail(row) {
    rowToSubmit.value = row;
    dialogVisible4.value = true;
}

const addDish = (row) => {
    const index = orderList.value.findIndex(item => item.dish_name === row.dish_name);
    if (index > -1) {
        orderList.value[index].count += 1;
    } else {
        const item = {
            dish_id: row.id,
            dish_name: row.dish_name,
            dish_price: row.dish_price,
            count: 1
        };
        orderList.value.push(item);
    }
    updateOrderPrice();
};

const updateOrderPrice = () => {
    let total = 0;
    if (orderList.value.length === 0) {
        OrderPrice.value = 0;
    } else {
        orderList.value.forEach(item => {
            total += item.dish_price * item.count;
        });
        OrderPrice.value = total;
    }
};

const addOrderItem = (index) => {
    if (orderList.value[index].count > 0) {
        orderList.value[index].count += 1;
    }
    updateOrderPrice();
};

const removeOrderItem = (index) => {
    if (orderList.value[index].count > 1) {
        orderList.value[index].count -= 1;
    } else {
        orderList.value.splice(index, 1);
    }
    updateOrderPrice();
};

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
    justify-content: center;
}

.flex-grow {
    flex-grow: 1;
}

.pagination-container {
    position: fixed;
    bottom: 4%;
    left: 35%;
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