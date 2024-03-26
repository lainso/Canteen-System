<template>
  <el-main class="error-page">
    <el-card class="error-card" shadow="hover">
      <img src="../assets/img/logo_circle.png" class="logo" alt="logo">
      <h1 class="system-name">内部餐饮系统</h1>
      <p class="error-message">啊噢，你要找的页面飞走啦，重新登录一下吧！</p>
      <el-button type="primary" @click="goBack">返回登录</el-button>
    </el-card>
  </el-main>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();
const goBack = () => {
  router.push('/login');
}

</script>

<style scoped>
.error-page {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f3f3f3;
}

.error-card {
  text-align: center;
  width: 100%;
  max-width: 600px;
}

.logo {
  max-width: 120px;
  margin-bottom: 24px;
}

.system-name {
  font-size: 24px;
  margin-bottom: 12px;
}

.error-message {
  margin-bottom: 24px;
}
</style>