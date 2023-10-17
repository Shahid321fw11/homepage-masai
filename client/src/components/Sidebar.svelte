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
	class="fixed flex flex-col p-6 top-0 right-0 h-screen w-full md:w-1/3 bg-[#ffffff] shadow-lg z-[201]"
>
	<div class="flex justify-end">
		<button
			class="w-[16px] h-[16px] inline-block leading-[1em] flex-shrink-0 align-middle"
			on:click={() => (isOpen = false)}
			><svg
				viewBox="0 0 24 30"
				focusable="false"
				class="w-[16px] h-[16px] inline-block leading-[1em] flex-shrink-0 align-middle"
				aria-hidden="true"
				><path
					fill="currentColor"
					d="M.439,21.44a1.5,1.5,0,0,0,2.122,2.121L11.823,14.3a.25.25,0,0,1,.354,0l9.262,9.263a1.5,1.5,0,1,0,2.122-2.121L14.3,12.177a.25.25,0,0,1,0-.354l9.263-9.262A1.5,1.5,0,0,0,21.439.44L12.177,9.7a.25.25,0,0,1-.354,0L2.561.44A1.5,1.5,0,0,0,.439,2.561L9.7,11.823a.25.25,0,0,1,0,.354Z"
				/></svg
			></button
		>
	</div>
	<div class="grid items-center h-full">
		<!-- Add more sidebar content as needed -->
		{#if signinRoute}
			<SignIn bind:togglesignIn={togglesignIn} />
		{:else}
			<Signup bind:togglesignIn={togglesignIn} />
		{/if}
	</div>
</div>
