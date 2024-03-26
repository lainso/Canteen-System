<template>
    <el-container style="height: 100vh;">
        <!-- 顶部导航栏 -->
        <el-header class="header-menu">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
                <img style="width: 60px; margin-left: 2rem;" src="../../assets/img/logo_circle.ico" alt="logo" />
                <el-menu-item @click="GoCus" index="1" style="font-weight: bold; margin-left: 3rem;"> 内 部 餐 饮 系 统 - 管
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
                    <el-menu default-active="1" class="el-menu-vertical-demo">
                        <el-menu-item index="1" @click="GoCus" style="width: 21vh;">
                            <el-icon>
                                <Avatar />
                            </el-icon>
                            <span>账户管理</span>
                        </el-menu-item>
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
                                <el-form-item label="账户名" prop="key" label-width="100px">
                                    <el-input v-model="form2.key" style="width: 350px;" clearable />
                                </el-form-item>
                                <el-form-item>
                                    <el-button @click="search(form2.key)" type="primary">搜索</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </div>
                    <h6 style="margin-left: 60vh; margin-top: 7px; color: red;">* 此账号仅用于清理管理员，若需要其它权限请使用普通管理员账号</h6>
                </el-card><br>
                <el-table :data="customers" style="width: 100%">
                    <el-table-column prop="username" label="账户名" />
                    <el-table-column prop="first_name" label="昵称" width="120"/>
                    <el-table-column prop="email" label="电子邮件" width="250"/>
                    <el-table-column prop="cus_tel" label="联系电话" />
                    <el-table-column prop="usertype" label="账户类型" />
                    <el-table-column prop="last_login" label="上次登录时间" />
                    <el-table-column label="操作" >
                        <template #default="scope">
                            <el-button type="info" size="small" @click="Detail(scope.row)">详情</el-button>

                            <el-button :disabled="scope.row.username === 'SuperAdminForSystem' " size="small" type="danger" @click="prepareDelete(scope.row)">删除</el-button>
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
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { $signout, $getSuperData, $delCus } from '@/api/super';
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
const rowToEdit = ref(null);
const dialogVisible = ref(false)
const dialogVisible2 = ref(false)
const dialogVisible3 = ref(false)
const dialogVisible4 = ref(false)
const dialogVisible5 = ref(false)
const total = ref(0);

const form2 = reactive({
    key: ''
})

const userTypeMappings = {
    super: "管理员",
};

const fixUserType = (usertype) => {
    return userTypeMappings[usertype] || usertype;
};

const getData = (key, pagenum) => {
    $getSuperData(key, 11, pagenum)
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

function Detail(row) {
    rowToEdit.value = row;
    dialogVisible4.value = true;
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

const GoCus = () => {
    router.push('/super/superAdmin');
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

.label {
    font-weight: bold;
    display: inline-block;
    min-width: 5rem;
    text-align: right;
    margin-right: .5rem;
}
</style>