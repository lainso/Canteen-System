import{$ as u,a as e}from"./request-DFAhraQF.js";const s=(c,i)=>new Promise((o,t)=>{e("api/super/account/signin",{username:c,password:i}).then(function(a){a.code===0?(location.href="#/super/index",o(a.data)):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),h=(c,i)=>new Promise((o,t)=>{e("api/super/account/signin",{username:c,password:i}).then(function(a){a.code===0?(location.href="#/super/superAdmin",o(a.data)):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),m=(c,i,o)=>new Promise((t,a)=>{e("api/super/account/reset",{username:c,old_pass:i,new_pass:o}).then(function(n){n.code===0?t(n.info):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),p=c=>new Promise((i,o)=>{e("api/super/account/resetDef",{username:c}).then(function(t){t.code===0?(location.href="#/super/login",i(t.data)):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),_=()=>new Promise((c,i)=>{u("api/super/account/signout",{}).then(function(o){o.code===0?(location.href="#/super/login",localStorage.clear(),sessionStorage.clear(),c(o.data)):(alert(o.info),i(o.data))}).catch(function(o){console.log(o),i(o)})}),g=(c,i,o)=>new Promise((t,a)=>{u("api/super/promo",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),P=c=>new Promise((i,o)=>{e("api/super/promo",{action:"delete",promo_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),y=(c,i,o,t,a)=>new Promise((n,d)=>{e("api/super/promo",{action:"add",promo_name:c,promo_code:i,promo_muti:o,promo_start:t,promo_end:a}).then(function(l){l.code===0?n(l.info):(alert(l.info),d(l.data))}).catch(function(l){console.log(l),d(l)})}),$=(c,i)=>new Promise((o,t)=>{e("api/super/promo",{action:"update",promo_id:c,promo_data:{promo_name:i.promo_name,promo_code:i.promo_code,promo_multi:i.promo_multiple,promo_start:i.promo_start,promo_end:i.promo_end}}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),w=(c,i,o)=>new Promise((t,a)=>{u("api/super/notice",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),D=c=>new Promise((i,o)=>{e("api/super/notice",{action:"delete",noti_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),b=(c,i,o)=>new Promise((t,a)=>{e("api/super/notice",{action:"add",username:c,noti_title:i,noti_content:o}).then(function(n){n.code===0?t(n.info):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),q=(c,i)=>new Promise((o,t)=>{e("api/super/notice",{action:"update",noti_id:c,noti_title:i.noti_title,noti_content:i.noti_content}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),r=(c,i,o)=>new Promise((t,a)=>{u("api/super/order",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),z=c=>new Promise((i,o)=>{e("api/super/order",{action:"delete",ord_number:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),S=(c,i)=>new Promise((o,t)=>{e("api/super/order",{action:"update",ord_number:c,ord_condition:i.ord_condition}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),k=(c,i,o)=>new Promise((t,a)=>{u("api/super/payment",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),C=c=>new Promise((i,o)=>{e("api/super/payment",{action:"delete",pay_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),v=(c,i)=>new Promise((o,t)=>{e("api/super/payment",{action:"update",pay_id:c,pay_money:i.pay_money,pay_way:i.pay_way}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),x=(c,i,o)=>new Promise((t,a)=>{u("api/super/paycard",{action:"query",username:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),E=c=>new Promise((i,o)=>{e("api/super/paycard",{action:"delete",card_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),N=(c,i)=>new Promise((o,t)=>{e("api/super/paycard",{action:"update",card_id:c,card_balance:i.card_balance,card_condition:i.card_condition}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),O=(c,i,o)=>new Promise((t,a)=>{u("api/super/customer",{action:"querySuper",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),A=(c,i,o)=>new Promise((t,a)=>{u("api/super/customer",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),L=c=>new Promise((i,o)=>{e("api/super/customer",{action:"delete",cus_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),B=c=>new Promise((i,o)=>{e("api/super/customer",{action:"add",username:c.username,password:c.password,email:c.email,fname:c.first_name,sex:c.cus_sex,tel:c.cus_tel,birth:c.cus_birth,address:c.cus_address,is_active:c.is_active,usertype:c.usertype}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),F=(c,i)=>new Promise((o,t)=>{e("api/super/customer",{action:"update",cus_id:c,cus_data:{email:i.email,fname:i.fname,sex:i.sex,tel:i.tel,birth:i.birth,address:i.address,is_active:i.is_active,usertype:i.usertype}}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),G=(c,i,o)=>new Promise((t,a)=>{u("api/super/employee",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),H=c=>new Promise((i,o)=>{e("api/super/employee",{action:"delete",emp_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),I=(c,i)=>new Promise((o,t)=>{e("api/super/employee",{action:"update",emp_id:c,emp_data:{emp_name:i.emp_name,emp_tel:i.emp_tel,emp_number:i.emp_number,emp_condition:i.emp_condition,emp_role:i.emp_role}}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),J=(c,i,o)=>new Promise((t,a)=>{u("api/super/dish",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),K=c=>new Promise((i,o)=>{e("api/super/dish",{action:"delete",dish_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),M=(c,i)=>new Promise((o,t)=>{e("api/super/dish",{action:"update",dish_id:c,dish_data:{dish_name:i.dish_name,dish_des:i.dish_des,dish_price:i.dish_price,dish_img:i.dish_img}}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),Q=(c,i,o)=>new Promise((t,a)=>{u("api/super/shop",{action:"query",keys:c,pagesize:i,pagenum:o}).then(function(n){n.code===0?t({data:n.list,total:n.total}):(alert(n.info),a(n.data))}).catch(function(n){console.log(n),a(n)})}),R=c=>new Promise((i,o)=>{e("api/super/shop",{action:"add",username:c.username,password:c.password,email:c.email,fname:c.shop_name,address:c.address,is_active:c.is_active,shop_name:c.shop_name,shop_tel:c.shop_tel,shop_head:c.shop_head,shop_pass:c.shop_pass}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),T=(c,i)=>new Promise((o,t)=>{e("api/super/shop",{action:"update",shop_id:c,shop_data:{shop_name:i.shop_name,shop_tel:i.shop_tel,shop_head:i.shop_head,shop_pass:i.shop_pass}}).then(function(a){a.code===0?o(a.info):(alert(a.info),t(a.data))}).catch(function(a){console.log(a),t(a)})}),U=c=>new Promise((i,o)=>{e("api/super/shop",{action:"delete",shop_id:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})}),V=c=>new Promise((i,o)=>{e("api/super/customer",{action:"resetShopPass",username:c}).then(function(t){t.code===0?i(t.info):(alert(t.info),o(t.data))}).catch(function(t){console.log(t),o(t)})});export{h as $,z as A,k as B,v as C,C as D,w as E,b as F,D as G,q as H,x as I,N as J,E as K,s as a,_ as b,O as c,L as d,p as e,g as f,y as g,P as h,$ as i,A as j,V as k,B as l,F as m,Q as n,R as o,T as p,U as q,m as r,G as s,I as t,H as u,J as v,M as w,K as x,r as y,S as z};