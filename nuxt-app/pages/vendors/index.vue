<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">Vendor Management</h1>
      <NuxtLink to="/vendors/create" class="btn-primary">
        Add Vendor
      </NuxtLink>
    </div>

    <!-- Vendors Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="card text-center">
        <div class="text-gray-400 py-12">
          <p class="text-lg mb-4">No vendors yet</p>
          <p class="text-sm">Click "Add Vendor" to add your first vendor</p>
        </div>
      </div>
    </div>
  </div>
</template>
