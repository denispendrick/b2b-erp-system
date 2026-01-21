<template>
  <div>
    <h1 class="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>

    <!-- KPI Cards -->
    <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
      <div class="card">
        <h3 class="text-sm font-medium text-gray-500">Total Sales</h3>
        <p class="mt-2 text-3xl font-semibold text-gray-900">$0.00</p>
      </div>
      <div class="card">
        <h3 class="text-sm font-medium text-gray-500">Inventory Value</h3>
        <p class="mt-2 text-3xl font-semibold text-gray-900">$0.00</p>
      </div>
      <div class="card">
        <h3 class="text-sm font-medium text-gray-500">Pending Orders</h3>
        <p class="mt-2 text-3xl font-semibold text-gray-900">0</p>
      </div>
      <div class="card">
        <h3 class="text-sm font-medium text-gray-500">Outstanding Invoices</h3>
        <p class="mt-2 text-3xl font-semibold text-gray-900">$0.00</p>
      </div>
    </div>

    <!-- Charts -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div class="card">
        <h2 class="text-lg font-semibold mb-4">Sales Trend</h2>
        <div class="h-64 flex items-center justify-center text-gray-400">
          Chart placeholder
        </div>
      </div>
      <div class="card">
        <h2 class="text-lg font-semibold mb-4">Order Status Distribution</h2>
        <div class="h-64 flex items-center justify-center text-gray-400">
          Chart placeholder
        </div>
      </div>
    </div>
  </div>
</template>
