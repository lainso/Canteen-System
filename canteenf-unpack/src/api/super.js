import { $get, $post } from "../utils/request";

export const $Login = (username, password) => {
    return new Promise((resolve, reject) => {
        $post('api/super/account/signin', {
            username: username,
            password: password
        })
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/super/index';
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

export const $SuperLogin = (username, password) => {
    return new Promise((resolve, reject) => {
        $post('api/super/account/signin', {
            username: username,
            password: password
        })
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/super/superAdmin';
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

export const $resetPass = (username, old_pass, new_pass) => {
    return new Promise((resolve, reject) => {
        $post('api/super/account/reset', {
            username: username,
            old_pass: old_pass,
            new_pass: new_pass
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $resetDefPass = (username) => {
    return new Promise((resolve, reject) => {
        $post('api/super/account/resetDef', {
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/super/login';
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
        $get('api/super/account/signout', {})
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/super/login';
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

export const $getPromoData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/promo', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delPromo = (promo_id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/promo', {
            action: 'delete',
            promo_id: promo_id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $addPromo = (promo_name, promo_code, promo_muti, promo_start, promo_end) => {
    return new Promise((resolve, reject) => {
        $post('api/super/promo', {
            action: 'add',
            promo_name: promo_name,
            promo_code: promo_code,
            promo_muti: promo_muti,
            promo_start: promo_start,
            promo_end: promo_end
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updatePromo = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/promo', {
            action: 'update',
            promo_id: id,
            promo_data: {
                promo_name: rows.promo_name,
                promo_code: rows.promo_code,
                promo_multi: rows.promo_multiple,
                promo_start: rows.promo_start,
                promo_end: rows.promo_end,
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getNotiData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/notice', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delNoti = (noti_id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/notice', {
            action: 'delete',
            noti_id: noti_id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $addNoti = (noti_cus, noti_title, noti_content) => {
    return new Promise((resolve, reject) => {
        $post('api/super/notice', {
            action: 'add',
            username: noti_cus,
            noti_title: noti_title,
            noti_content: noti_content
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateNoti = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/notice', {
            action: 'update',
            noti_id: id,
            noti_title: rows.noti_title,
            noti_content: rows.noti_content
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getOrderData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/order', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delOrder = (ord_number) => {
    return new Promise((resolve, reject) => {
        $post('api/super/order', {
            action: 'delete',
            ord_number: ord_number
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateOrder = (ord_num, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/order', {
            action: 'update',
            ord_number: ord_num,
            ord_condition: rows.ord_condition
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getPayData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/payment', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delPay = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/payment', {
            action: 'delete',
            pay_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updatePay = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/payment', {
            action: 'update',
            pay_id: id,
            pay_money: rows.pay_money,
            pay_way: rows.pay_way
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getCardData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/paycard', {
            action: 'query',
            username: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delCard = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/paycard', {
            action: 'delete',
            card_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateCard = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/paycard', {
            action: 'update',
            card_id: id,
            card_balance: rows.card_balance,
            card_condition: rows.card_condition
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getSuperData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/customer', {
            action: 'querySuper',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $getCusData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/customer', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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
        $post('api/super/customer', {
            action: 'delete',
            cus_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $addCus = (form) => {
    return new Promise((resolve, reject) => {
        $post('api/super/customer', {
            action: 'add',
            username: form.username,
            password: form.password,
            email: form.email,
            fname: form.first_name,
            sex: form.cus_sex,
            tel: form.cus_tel,
            birth: form.cus_birth,
            address: form.cus_address,
            is_active: form.is_active,
            usertype: form.usertype
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateCus = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/customer', {
            action: 'update',
            cus_id: id,
            cus_data: {
                email:rows.email,
                fname:rows.fname,
                sex:rows.sex,
                tel:rows.tel,
                birth:rows.birth,
                address:rows.address,
                is_active:rows.is_active,
                usertype:rows.usertype,
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getEmpData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/employee', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delEmp = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/employee', {
            action: 'delete',
            emp_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateEmp = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/employee', {
            action: 'update',
            emp_id: id,
            emp_data: {
                emp_name:rows.emp_name,
                emp_tel:rows.emp_tel,
                emp_number:rows.emp_number,
                emp_condition:rows.emp_condition,
                emp_role:rows.emp_role
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getDishData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/dish', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $delDish = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/dish', {
            action: 'delete',
            dish_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateDish = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/dish', {
            action: 'update',
            dish_id: id,
            dish_data: {
                dish_name:rows.dish_name,
                dish_des:rows.dish_des,
                dish_price:rows.dish_price,
                dish_img:rows.dish_img
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $getShopData = (key, pagesize, pagenum) => {
    return new Promise((resolve, reject) => {
        $get('api/super/shop', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({data:response.list, total:response.total});
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

export const $addShop = (form) => {
    return new Promise((resolve, reject) => {
        $post('api/super/shop', {
            action: 'add',
            username: form.username,
            password: form.password,
            email: form.email,
            fname: form.shop_name,
            address: form.address,
            is_active: form.is_active,
            shop_name: form.shop_name,
            shop_tel: form.shop_tel,
            shop_head: form.shop_head,
            shop_pass: form.shop_pass,
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $updateShop = (id, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/super/shop', {
            action: 'update',
            shop_id: id,
            shop_data: {
                shop_name: rows.shop_name,
                shop_tel: rows.shop_tel,
                shop_head: rows.shop_head,
                shop_pass: rows.shop_pass,
            }
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $delShop = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/super/shop', {
            action: 'delete',
            shop_id: id
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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

export const $resetShopPass = (username) => {
    return new Promise((resolve, reject) => {
        $post('api/super/customer', {
            action: 'resetShopPass',
            username: username
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve(response.info);
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