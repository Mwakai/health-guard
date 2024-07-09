<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const user = ref(null)
const recommendations = ref([])

const fetchUserAndRecommendations = async () => {
  try {
    // Replace with actual user email or ID as needed
    const response = await axios.get('http://localhost:5000/api/user', {
      params: { email: 'user@example.com' }
    })
    user.value = response.data.user

    // Fetch dietary supplement recommendations based on user data
    const recResponse = await axios.get('http://localhost:5000/api/recommendations', {
      params: {
        age: user.value.age,
        height: user.value.height,
        weight: user.value.weight,
        allergies: user.value.allergies
      }
    })
    recommendations.value = recResponse.data.recommendations
  } catch (error) {
    console.error('Error fetching user data or recommendations:', error)
  }
}

onMounted(fetchUserAndRecommendations)
</script>

<template>
  <div>
    <h1>Welcome to your Dashboard</h1>
    <h1>Im a user</h1>
    <div v-if="user">
      <p>Age: {{ user.age }}</p>
      <p>Height: {{ user.height }}</p>
      <p>Weight: {{ user.weight }}</p>
      <p>Allergies: {{ user.allergies }}</p>
    </div>
    <div v-if="recommendations.length">
      <h2>Recommended Dietary Supplements</h2>
      <ul>
        <li v-for="rec in recommendations" :key="rec.id">{{ rec.name }}: {{ rec.description }}</li>
      </ul>
    </div>
  </div>
</template>
