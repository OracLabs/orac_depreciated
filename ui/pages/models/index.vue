<template>
  <div>
    <table>
      <tr>
        <th>Name</th>
      </tr>
      <tr v-for="model in models">
        <td>
          <NuxtLink :to="`models/${model.id}`">{{ model.name }}</NuxtLink>
        </td>
      </tr>
    </table>
  </div>
</template>

<script setup>
const { data: models } = await useFetch("http://localhost:8000/api/models");
</script>
