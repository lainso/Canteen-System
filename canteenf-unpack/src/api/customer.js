import { $get, $post } from "../utils/request";

export const $Login = (username, password) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/account/signin', {
            username: username,
            password: password
        })
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/index';
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $Register = (username, password, name, email, sex, birth, tel) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/account/register', {
            username: username,
            password: password,
            name: name,
            email: email,
            sex: sex,
            birth: birth,
            tel: tel
        })
            .then(function (response) {
                if (response.code === 0) {
                    alert("注册成功，验证码已发送到您的邮箱！")
                    location.href = '#/active';
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $activate = (v_code, username) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/account/active', {
            code: v_code,
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    alert("激活成功！")
                    location.href = '#/login';
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $resetPass = (email) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/account/resetPass', {
            email: email
        })
            .then(function (response) {
                if (response.code === 0) {
                    alert("邮件发送成功！请前往邮箱获取重置验证码。")
                    location.href = '#/resetDone';
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $resetDone = (password, v_code, email) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/account/resetDone', {
            email: email,
            password: password,
            code: v_code
        })
            .then(function (response) {
                if (response.code === 0) {
                    alert("重置密码成功！请使用新密码登录。")
                    location.href = '#/login';
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $signout = () => {
    return new Promise((resolve, reject) => {
        $get('api/customer/account/signout', {})
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/login';
                    localStorage.clear();
                    sessionStorage.clear();
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $getMyInfo = (username) => {
    return new Promise((resolve, reject) => {
        $get('api/customer/customer', {
            action: 'query',
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.list);
                    // console.log(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $delCus = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/customer', {
            action: 'delete',
            cus_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    alert("删除成功！")
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $updateCus = (id, form) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/customer', {
            action: 'update',
            cus_id: id,
            cus_data: {
                fname: form.fname,
                tel: form.tel,
                sex: form.sex,
                birth: form.birth,
                address: form.address,
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.info);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $applyCard = (username) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/paycard', {
            action: 'register',
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $activeCard = (id, code) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/paycard', {
            action: 'active',
            card_id: id,
            code: code
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $delCard = (card_num) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/paycard', {
            action: 'delete',
            card_number: card_num
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $updateCard = (card_num, money, promo_code) => {
    return new Promise((resolve, reject) => {
        $post('api/customer/paycard', {
            action: 'update',
            card_number: card_num,
            money: money,
            code: promo_code
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $getCardInfo = (username) => {
    return new Promise((resolve, reject) => {
        $get('api/customer/paycard', {
            action: 'query',
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.data);
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $getOrderInfo = (username, start_time, end_time, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/customer/order', {
            username: username,
            start_time: start_time,
            end_time: end_time,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.data, total:response.total});
                } else {
                    alert(response.msg);
                    reject(response.data);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}

export const $getNotiInfo = (username, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/customer/notice', {
            username: username,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
                } else {
                    alert(response.info);
                    reject(response.list);
                }
            })
            .catch(function (error) {
                console.log(error);
                reject(error);
            });
    });
}