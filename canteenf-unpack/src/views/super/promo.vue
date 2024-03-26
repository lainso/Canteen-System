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
                    <el-menu default-active="7" class="el-menu-vertical-demo">
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
                                    <el-button type="success" @click="dialogVisible2 = true;">新增促销</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                        <!-- 搜索区域容器 -->
                        <div class="search-area">
                            <el-form :inline="true" :model="form2" label-width="20%"
                                class="demo-form-inline search-form" status-icon>
                                <el-form-item label="优惠名称" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                </el-card><br>
                <el-table :data="promos" style="width: 100%">
                    <el-table-column prop="promo_name" label="名称" width="140" />
                    <el-table-column prop="promo_multiple" label="优惠倍率" width="150" />
                    <el-table-column prop="promo_code" label="促销码" />
                    <el-table-column prop="promo_start" label="开始时间" />
                    <el-table-column prop="promo_end" label="结束时间" />
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
                    <span>此操作不可逆！是否确认删除该促销？</span>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="danger" @click="confirmDelete">
                                确认
                            </el-button>
                        </div>
                    </template>
                </el-dialog>
                <el-dialog style="margin-right: 58vh; margin-top: 25vh;" v-model="dialogVisible2" title="新建促销"
                    width="500">
                    <br>
                    <el-form ref="ruleFormRef" :model="form" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="促销名称" prop="promo_name">
                            <el-input v-model="form.promo_name" />
                        </el-form-item>
                        <el-form-item label="促销码" prop="promo_code">
                            <el-input v-model="form.promo_code" />
                        </el-form-item>
                        <el-form-item label="优惠倍率" prop="promo_multiple">
                            <el-input v-model="form.promo_multiple" />
                        </el-form-item>
                        <el-form-item label="开始时间" prop="promo_start">
                            <el-date-picker v-model="form.promo_start" type="date" clearable />
                        </el-form-item>
                        <el-form-item label="结束时间" prop="promo_end">
                            <el-date-picker v-model="form.promo_end" type="date" clearable />
                        </el-form-item>
                    </el-form>

                    <template #footer>
                        <div class="dialog-footer">
                            <el-button @click="dialogVisible2 = false; onReset(ruleFormRef)">取消</el-button>
                            <el-button type="success" @click="createPromo(ruleFormRef)">
                                确认新增
                            </el-button>
                        </div>
                    </template>
                </el-dialog>

                <el-dialog style="margin-right: 58vh; margin-top: 25vh;" v-model="dialogVisible3" title="促销信息修改"
                    width="500">
                    <br>
                    <el-form ref="ruleFormRef3" :model="form3" :rules="rule" label-width="17%" class="demo-form"
                        status-icon>
                        <el-form-item label="促销名称" prop="promo_name">
                            <el-input v-model="form3.promo_name" />
                        </el-form-item>
                        <el-form-item label="促销码" prop="promo_code">
                            <el-input v-model="form3.promo_code" />
                        </el-form-item>
                        <el-form-item label="优惠倍率" prop="promo_multiple">
                            <el-input v-model="form3.promo_multiple" />
                        </el-form-item>
                        <el-form-item label="开始时间" prop="promo_start">
                            <el-date-picker v-model="form3.promo_start" type="date" clearable />
                        </el-form-item>
                        <el-form-item label="结束时间" prop="promo_end">
                            <el-date-picker v-model="form3.promo_end" type="date" clearable />
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
import { $signout, $getPromoData, $delPromo, $addPromo, $updatePromo } from '@/api/super';
import {
    Document, Avatar, ForkSpoon,
    ChatDotSquare, DocumentChecked,
    CreditCard,
    Setting, HomeFilled
} from '@element-plus/icons-vue'

const activeIndex = ref('1');
const router = useRouter();
const promos = ref([]);
const currentPage1 = ref(1);
const rowToDelete = ref(null);
const rowToEdit = ref(null);
const ruleFormRef = ref(null);
const ruleFormRef3 = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const total = ref(0);

const createPromo = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            $addPromo(form.promo_name, form.promo_code, form.promo_multiple, form.promo_start, form.promo_end)
                .then(function (data) {
                    if(confirm('新增促销活动成功，是否前往发布通知？')){
                        location.href = '#/super/noti';
                    }
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

const form2 = reactive({
    key: ''
})

const form = reactive({
    promo_name: '',
    promo_code: '',
    promo_multiple: '',
    promo_start: '',
    promo_end: ''
})

const form3 = reactive({
    promo_name: '',
    promo_code: '',
    promo_multiple: '',
    promo_start: '',
    promo_end: ''
})

const validate_multiple = (rule, value, callback) => {
    const n = Number(value);
    if (isNaN(n)) {
        return callback(new Error('促销倍率必须是一个数字'));
    }
    if (n < 1) {
        return callback(new Error('促销倍率需要大于1，否则会反向优惠。'));
    }
    return callback();
};

const rule = reactive({
    promo_name: [
        { required: true, message: '促销名称不能为空', trigger: 'blur' },
    ],
    promo_code: [
        { required: true, message: '促销码不能为空', trigger: 'blur' },
    ],
    promo_multiple: [
        { required: true, message: '促销倍率不能为空', trigger: 'blur' },
        { validator: validate_multiple, message: '促销倍率必须为一个大于1的数字', trigger: ['blur'] },
    ],
    promo_start: [
        { required: true, message: '促销开始时间不能为空', trigger: 'blur' },
    ],
    promo_end: [
        { required: true, message: '促销结束时间不能为空', trigger: 'blur' },
    ]
})

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

function prepareDelete(row) {
    rowToDelete.value = row;
    dialogVisible.value = true;
}

function prepareEdit(row) {
    rowToEdit.value = row;
    Object.keys(form3).forEach(key => {
        form3[key] = row[key] ?? "";
    });
    dialogVisible3.value = true;
}

const editPromo = (promoid, editedRow) => {
    console.log(promoid, editedRow);
    $updatePromo(promoid, editedRow)
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

function confirmEdit() {
    if (!ruleFormRef3.value || !rowToEdit.value) return;
    
    ruleFormRef3.value.validate((valid) => {
        if (valid) {
            // 我们创建一个新的对象来存储传递给更新 API 的数据，并且添加 id 字段
            let editedData = {
                promo_name: form3.promo_name,
                promo_code: form3.promo_code,
                promo_multiple: form3.promo_multiple,
                promo_start: form3.promo_start,
                promo_end: form3.promo_end
            };

            // 从 rowToEdit 中获取当前促销活动的 id
            const promoId = rowToEdit.value.id;

            // 传递 id 和编辑后的新数据给 editPromo 方法
            editPromo(promoId, editedData);
            dialogVisible3.value = false;
        } else {
            // 处理表单验证不通过的情况
            console.log("编辑表单验证失败");
        }
    });
}

function confirmDelete() {
    if (rowToDelete.value) {
        handleDelete(rowToDelete.value);
    }
    dialogVisible.value = false;
}

const handleDelete = (rows) => {
    $delPromo(rows.id)
        .then(function (info) {
            alert(info);
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

const getData = (key, pagenum) => {
    $getPromoData(key, 11, pagenum)
        .then(function (response) {
            promos.value = response.data.map(promo => {
                promo.promo_start = fixTime(promo.promo_start);
                promo.promo_end = fixTime(promo.promo_end);
                return promo;
            });
            total.value = response.total;
            total.value = response.total;
        })
        .catch(function (error) {
            console.log(error);
        });
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