<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">Invoices</h1>
      <NuxtLink to="/invoices/create" class="btn-primary">
        Create Invoice
      </NuxtLink>
    </div>

    <!-- Filter and Search -->
    <div class="card mb-6">
      <div class="flex gap-4">
        <input type="text" placeholder="Search invoices..." class="input flex-1" />
        <select class="input w-48">
          <option>All Statuses</option>
          <option>Draft</option>
          <option>Sent</option>
          <option>Paid</option>
          <option>Overdue</option>
        </select>
      </div>
    </div>

    <!-- Invoices Table -->
    <div class="card">
      <div class="overflow-x-auto">
        <table class="table">
          <thead>
            <tr>
              <th class="table-header">Invoice #</th>
              <th class="table-header">Customer</th>
              <th class="table-header">Invoice Date</th>
              <th class="table-header">Due Date</th>
              <th class="table-header">Amount</th>
              <th class="table-header">Paid</th>
              <th class="table-header">Balance</th>
              <th class="table-header">Status</th>
              <th class="table-header">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr>
              <td class="table-cell" colspan="9">
                <div class="text-center py-8 text-gray-500">
                  No invoices found. Click "Create Invoice" to generate your first invoice.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
