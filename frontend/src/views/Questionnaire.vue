<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('') // You can pass the email from the login or registration process
const age = ref<number | null>(null)
const height = ref<number | null>(null)
const weight = ref<number | null>(null)
const allergies = ref('')

const submitQuestionnaire = async () => {
  try {
    const response = await axios.post('http://localhost:5000/api/questionnaire', {
      email: email.value,
      age: age.value,
      height: height.value,
      weight: weight.value,
      allergies: allergies.value
    })
    console.log(response.data.message)
    // Handle successful questionnaire submission (e.g., redirect to dashboard)
    router.push('/dashboard')
  } catch (error) {
    console.error('Error submitting questionnaire:', error)
    if (error.response) {
      console.error('Backend response:', error.response.data)
    }
  }
}
</script>

<template>
  <h1>Questionnaire</h1>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Fill out the questionnaire
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="submitQuestionnaire">
        <div>
          <label for="age" class="block text-sm font-medium leading-6 text-gray-900">Age</label>
          <div class="mt-2">
            <input
              v-model="age"
              id="age"
              name="age"
              type="number"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label for="height" class="block text-sm font-medium leading-6 text-gray-900"
            >Height (cm)</label
          >
          <div class="mt-2">
            <input
              v-model="height"
              id="height"
              name="height"
              type="number"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label for="weight" class="block text-sm font-medium leading-6 text-gray-900"
            >Weight (kg)</label
          >
          <div class="mt-2">
            <input
              v-model="weight"
              id="weight"
              name="weight"
              type="number"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label for="allergies" class="block text-sm font-medium leading-6 text-gray-900"
            >Allergies</label
          >
          <div class="mt-2">
            <input
              v-model="allergies"
              id="allergies"
              name="allergies"
              type="text"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
