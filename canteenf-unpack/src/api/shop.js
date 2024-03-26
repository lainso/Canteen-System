import { $get, $post } from "../utils/request";

export const $Login = (username, password) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/account/signin', {
            username: username,
            password: password
        })
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/shop/index';
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
        $get('api/shop/account/signout', {})
            .then(function (response) {
                if (response.code === 0) {
                    location.href = '#/shop/login';
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

export const $resetPass = (username, old_pass, new_pass) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/account/reset', {
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

export const $getMyInfo = (username) => {
    return new Promise((resolve, reject) => {
        $get('api/shop/shop', {
            action: 'query',
            username: username
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

export const $updateShop = (username, form) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/shop', {
            action: 'update',
            username: username,
            data: {
                shop_name: form.shop_name,
                shop_tel: form.shop_tel,
                shop_head: form.shop_head,
                shop_pass: form.shop_pass,
                email: form.email,
                address: form.cus_address,
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

export const $getDishData = (key, pagesize, pagenum, username) => {
    return new Promise((resolve, reject) => {
        $get('api/shop/dish', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum,
            username: username
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

export const $addDish = (username, form) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/dish', {
            action: 'add',
            username: username,
            dish_name: form.dish_name,
            dish_price: form.dish_price,
            dish_des: form.dish_des,
            dish_img: form.dish_img
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

export const $delDish = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/dish', {
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

export const $getEmpData = (key, pagesize, pagenum, username) => {
    return new Promise((resolve, reject) => {
        $get('api/shop/employee', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum,
            username: username
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

export const $addEmp = (username, form) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/employee', {
            action: 'add',
            username: username,
            emp_name: form.emp_name,
            emp_number: form.emp_number,
            emp_tel: form.emp_tel,
            emp_condition: form.emp_condition,
            emp_role: form.emp_role,
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

export const $delEmp = (id) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/employee', {
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
                emp_name: rows.emp_name,
                emp_tel: rows.emp_tel,
                emp_number: rows.emp_number,
                emp_condition: rows.emp_condition,
                emp_role: rows.emp_role,
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

export const $getOrderData = (key, pagesize, pagenum, username) => {
    return new Promise((resolve, reject) => {
        $get('api/shop/order', {
            action: 'query',
            keys: key,
            pagesize: pagesize,
            pagenum: pagenum,
            username: username
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

export const $updateOrder = (ord_num, rows) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/order', {
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

export const $addOrder = (data) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/order', {
            action: 'add',
            username: data.username,
            user: data.user,
            ord_condition: data.ord_condition,
            ord_list: data.ord_list,
            money: data.money,
        })
            .then(function (response) {
                if (response.code === 0) {
                    resolve({'info':response.info, 'id': response.id});
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

export const $addPayment = (data) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/payment', {
            pay_money: data.money,
            pay_way: data.pay_way,
            ord_id: data.ord_id,
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

export const $updatePaycard = (data) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/paycard', {
            username: data.username,
            money: data.money
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

export const $joinShop = (form) => {
    return new Promise((resolve, reject) => {
        $post('api/shop/joinShop', {
            emp_name: form.emp_name,
            emp_tel: form.emp_tel,
            shop_pass: form.shop_pass
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