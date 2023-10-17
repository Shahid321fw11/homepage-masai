<script>
	export let data = {
		full_name: '',
		email: '',
		phone_number: '',
		referral_code: '',
		password: ''
	};

	export let togglesignIn;
</script>

<!-- <main class=" flex flex-col gap-3"> -->

<div class="flex flex-col gap-4">
	<div>
		<p>Full Name <span class="text-[#ff3561]">*</span></p>
		<input
			class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
			type="text"
			placeholder="Enter your Full name"
			bind:value={data.full_name}
		/>
	</div>
	<div>
		<p>Email address <span class="text-[#ff3561]">*</span></p>
		<input
			class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
			type="text"
			placeholder="Enter email address"
			bind:value={data.email}
		/>
	</div>
	<div>
		<p>Phone Number <span class="text-[#ff3561]">*</span></p>
		<input
			class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
			type="text"
			placeholder="Enter phone number"
			bind:value={data.phone_number}
		/>
	</div>
	<div>
		<p>Referral Code (Optional)</p>
		<input
			class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
			type="text"
			placeholder="Enter referral code"
			bind:value={data.referral_code}
		/>
	</div>
	<div>
		<p>Password <span class="text-[#ff3561]">*</span></p>
		<input
			class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
			type="password"
			placeholder="Enter your password"
			bind:value={data.password}
		/>
	</div>
	
</div>
<!-- </main> -->
