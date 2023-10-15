<script>
	import SignIn from './SignIn.svelte';
	import Signup from './Signup.svelte';

	export let isOpen;
	let signinRoute = false;
	let togglesignIn = () => {
		signinRoute = !signinRoute;
	};
</script>

<div
	class="fixed flex flex-col p-6 top-0 right-0 h-screen w-full md:w-1/3 bg-[#ffffff] transform scale-70 shadow-lg z-[201]"
>
	<div class="flex justify-end">
		<button class="text-[#ec0532] hover:bg-slate-50 p-4" on:click={() => (isOpen = false)}
			><svg
				class="w-3 h-3 text-gray-800 dark:text-white"
				aria-hidden="true"
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 14 14"
			>
				<path
					stroke="currentColor"
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
				/>
			</svg></button
		>
	</div>
	<!-- Add more sidebar content as needed -->
	{#if signinRoute}
		<SignIn {togglesignIn} />
	{:else}
		<Signup {togglesignIn} />
	{/if}
</div>
