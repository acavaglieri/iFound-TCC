<template>
    <div id="login">
        <h1>Login</h1>
        <input type="email" name="email" v-model="input.email" placeholder="email" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        input: {
          email: "",
          password: ""
        }
      }
    },
    methods: {
      login() {
        if(this.input.email != "" && this.input.password != "") {
          if(this.input.email == this.$parent.mockAccount.email && this.input.password == this.$parent.mockAccount.password) {
            this.$emit("authenticated", true);
            this.$router.replace({ name: "secure" });
          } else {
            // eslint-disable-next-line
            console.log("The email and / or password is incorrect");
          }
        } else {
          // eslint-disable-next-line
          console.log("A email and password must be present");
        }
      }
    }
  }
</script>

<style scoped>
  #login {
    width: 500px;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: auto;
    margin-top: 200px;
    padding: 20px;
  }
</style>