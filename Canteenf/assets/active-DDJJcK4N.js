import{_ as h}from"./logo-BME6R_gW.js";import{d as x}from"./customer-DbI0IaiP.js";import{u as k}from"./userStore-DWnd3T38.js";import{_ as y}from"./_plugin-vue_export-helper-DlAUqK2U.js";import{r as V,a as m,c as S,b as l,e as t,w as a,d as r,q as C,f as c,o as I,p as w,g as N}from"./index-BA2o8hTc.js";import"./request-IzQaM4-z.js";const B="/assets/active_back-DJIxzsyJ.jpg",U=n=>(w("data-v-6cc5b5d2"),n=n(),N(),n),q={class:"login"},F=U(()=>l("img",{class:"left",src:B,alt:"left poster"},null,-1)),J={class:"box"},R=C('<div class="logo-container" data-v-6cc5b5d2><img class="logo" src="'+h+'" alt="left poster" data-v-6cc5b5d2><span class="logo-text" data-v-6cc5b5d2>内部餐饮系统</span></div><div style="display:flex;text-align:center;" data-v-6cc5b5d2><p class="title" data-v-6cc5b5d2>账号激活</p></div>',2),$={class:"info"},j={class:"contact"},z={__name:"active",setup(n){const i=V(),o=m({v_code:"",username:k().getUsername}),u=m({v_code:[{required:!0,message:"验证码不能为空",trigger:"blur"}]}),f=d=>{d&&d.validate(e=>{if(e)x(o.v_code,o.username).then(function(s){console.log(s)}).catch(function(s){console.log(s)});else return!1})};return(d,e)=>{const s=c("el-input"),_=c("el-form-item"),v=c("el-button"),b=c("el-form"),g=c("el-link");return I(),S("div",q,[F,l("div",J,[R,t(b,{ref_key:"ruleFormRef",ref:i,model:o,rules:u,"label-width":"20%",class:"demo-form","status-icon":""},{default:a(()=>[t(_,{label:"验证码",prop:"v_code"},{default:a(()=>[t(s,{modelValue:o.v_code,"onUpdate:modelValue":e[0]||(e[0]=p=>o.v_code=p)},null,8,["modelValue"])]),_:1}),t(_,null,{default:a(()=>[t(v,{type:"success",onClick:e[1]||(e[1]=p=>f(i.value))},{default:a(()=>[r(" 激活 ")]),_:1})]),_:1})]),_:1},8,["model","rules"]),l("div",$,[l("p",null,[r("Copyright © 2024 lains. "),l("span",j,[r("Contact me ："),t(g,{underline:!1,type:"success",href:"https://github.com/lainso",target:"_blank"},{default:a(()=>[r("Github")]),_:1})])])])])])}}},K=y(z,[["__scopeId","data-v-6cc5b5d2"]]);export{K as default};