<script setup>

    let question = ref("")

    const sendMessage = () => {
        alert("Button was clicked: " + question.value);
    }

</script>


<template>
    <div>
        <h1>ChatBot do Senai!</h1>
        <label for ="">Type here your message!</label> <br><br>
        <input type="text" v-model="question"> <br><br>
        <button @click="sendMessage">Send</button>
    </div>
</template>

<style scoped>
    button{
        background-color: black;
        color: white;

    }
</style>