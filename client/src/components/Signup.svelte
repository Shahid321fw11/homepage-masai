<script>
	export let togglesignIn;

	let data = {
		name: '',
		email: '',
		mobile: '',
		code: '',
		password: ''
	};
	function handleSubmit() {
		console.log('Submitting data:', data);
	}
	function handleKeyDown(event) {
		handleSubmit();
	}

	$: {
		console.log(data);
	}
</script>

<main class=" flex flex-col gap-3">
	<div class="text-center">
		<h1 class="text-3xl font-medium">Create Account</h1>
		<p class="text-lg font-medium">
			Already have an account? <span
				class="text-[#4358F6] hover:underline hover:cursor-pointer"
				on:click={togglesignIn}
				on:keydown={handleKeyDown}
				tabindex="0"
				role="button">Sign In</span
			>
		</p>
	</div>

	<div class="flex flex-col gap-4">
		<div>
			<p>Full Name <span class="text-[#ff3561]">*</span></p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter your Full name"
				bind:value={data.name}
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
				type="number"
				placeholder="Enter phone number"
				bind:value={data.mobile}
			/>
		</div>
		<div>
			<p>Referral Code (Optional)</p>
			<input
				class="border border-1 border-[#f0f4f7] rounded-lg h-12 w-full px-2"
				type="text"
				placeholder="Enter referral code"
				bind:value={data.code}
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
		<button
			on:click={handleSubmit}
			class="w-full rounded-md bg-[#3470e3] text-[#ffffff] border border-1 h-12">SUBMIT</button
		>
		<p class="text-center text-sm">
			By signing up, I accept the Masai <a
				class="text-[#4358F6] underline"
				href="https://masaischool.com/terms">Terms of Service</a
			>
			and acknowledge the
			<a class="text-[#4358F6] underline" href="https://masaischool.com/privacy">Privacy Policy</a>.
		</p>
	</div>
</main>
