import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Welcome back, Jane', 'Welcome back, Admin')
content = content.replace('Your next move is just a click away. Track, request, and manage everything.', 'Here is the overview of all shifting operations and system metrics.')
content = content.replace('Jane Doe', 'Admin User')
content = content.replace('Customer', 'System Administrator')

# Sidebar replacements
content = content.replace('My Requests', 'All Bookings')
content = content.replace('Live Tracking', 'Manage Crew')
content = content.replace('Invoices', 'Finance & Revenue')
content = content.replace('Profile', 'Platform Settings')

# Top stats
content = content.replace('Active Moves', 'Total Active Jobs')
content = content.replace('Total Shifts', 'Total Completed Jobs')
content = content.replace('Packed Items', 'Available Crews')
content = re.sub(r'<p class="text-3xl font-black mt-1">46</p>\s*<p class="text-xs text-amber-600 mt-2">\+12 fragile items</p>', '<p class="text-3xl font-black mt-1">12</p><p class="text-xs text-amber-600 mt-2">3 crews on leave</p>', content)
content = content.replace('Pending Invoices', 'Total Revenue')
content = content.replace('1,240', '45,240')
content = content.replace('2 invoices due', '+15% from last month')

# All Bookings Section
content = re.sub(r'<div id="requests" class="admin-section hidden">.*?</div>\s*</div>\s*</div>', 
'''<div id="requests" class="admin-section hidden">
        <div class="dashboard-card p-6 reveal">
          <h2 class="text-2xl font-serif font-bold mb-2"><span class="text-accent">??</span> All Bookings</h2>
          <p class="text-secondary-text mb-6">Manage all customer bookings across the platform.</p>
          <div class="overflow-x-auto">
            <table class="w-full text-sm text-left">
              <thead class="border-b border-border text-secondary-text text-xs uppercase tracking-wider">
                <tr><th class="pb-3">Customer</th><th class="pb-3">Route</th><th class="pb-3">Status</th><th class="pb-3">Action</th></tr>
              </thead>
              <tbody class="divide-y divide-border">
                <tr>
                  <td class="py-4 font-bold">John Smith</td>
                  <td class="py-4">NYC ? LA</td>
                  <td class="py-4"><span class="badge-warning px-3 py-1 rounded-full text-xs font-bold">Pending</span></td>
                  <td class="py-4"><button class="btn-accent px-4 py-1 rounded text-xs">Assign Crew</button></td>
                </tr>
                <tr>
                  <td class="py-4 font-bold">Alice Wong</td>
                  <td class="py-4">Chicago ? Detroit</td>
                  <td class="py-4"><span class="badge-success px-3 py-1 rounded-full text-xs font-bold">In Transit</span></td>
                  <td class="py-4"><button class="text-accent hover:underline font-bold text-xs">Track</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>''', content, flags=re.DOTALL)

# Manage Crew Section
content = re.sub(r'<div id="tracking" class="admin-section hidden">.*?</div>\s*</div>\s*</div>',
'''<div id="tracking" class="admin-section hidden">
        <div class="dashboard-card p-6 reveal">
          <h2 class="text-2xl font-serif font-bold mb-2"><span class="text-accent">??</span> Manage Crew</h2>
          <p class="text-secondary-text mb-6">Overview of all active crews and their availability.</p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="dashboard-card p-6 border-l-4 border-l-emerald-500">
              <h4 class="font-bold">Team Alpha</h4>
              <p class="text-sm text-secondary-text mt-1">Status: Available</p>
              <button class="mt-4 text-accent text-sm font-bold">View Schedule</button>
            </div>
            <div class="dashboard-card p-6 border-l-4 border-l-amber-500">
              <h4 class="font-bold">Team Bravo</h4>
              <p class="text-sm text-secondary-text mt-1">Status: On Job #MOV-5092</p>
              <button class="mt-4 text-accent text-sm font-bold">Track Team</button>
            </div>
          </div>
        </div>
      </div>''', content, flags=re.DOTALL)

content = content.replace('Itemized Invoices', 'Finance & Revenue')
content = content.replace('Full charge breakdown for your completed shifts.', 'Overview of platform revenue, pending payouts and outstanding invoices.')

content = content.replace('My Profile', 'Platform Settings')
content = content.replace('Update Profile', 'Save Settings')
content = content.replace('Jane Doe', 'Admin')
content = content.replace('jane@shiftora.com', 'admin@shiftora.com')
content = content.replace('123 Brooklyn Ave, NYC', 'Shiftora HQ')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
