<script setup>
    let message = ref("")
    let response = ref("")
    const sendMenssage = async () => {
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: message
            }
        })
    }
</script>

<template>
    <div>
        <label for=""> Type here your message!</label> <br>
        <textarea v-model="message"/> <br> <br>
        <button @click="sendMenssage"> Send</button>
    </div>
    
    <div>
        <h4>Response: </h4>
        <p>{{ answer }}</p>
    </div>

</template>

<style scoped>
     
    button{
        background-color: black;
        color: white;
    }
</style>