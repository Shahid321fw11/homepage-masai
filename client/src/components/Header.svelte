<script>
	import { onMount } from 'svelte';
	import Signup from './Signup.svelte';
	let isOpen = false;

	const toggleSidebar = () => {
		isOpen = !isOpen;
	};
	onMount(() => {
		isOpen = false;
	});
</script>

<main class="w-full position-sticky top-0 z-30 ">
	<div class="p-1 flex justify-center items-center gap-2 bg-[#fedfe5] text-md border">
		<p class="font-normal text-lg">Applications for our 6th November Batches are now open!</p>
		<button
			class="p-[8px] border border-red-500 border-1 bg-[#db022e] text-[#ffffff] text-md rounded-lg"
			>APPLY NOW</button
		>
	</div>
	<!-- border-red-500 border-1 p-1 -->
	<div class="flex justify-between border px-12 py-4">
		<img
			class="object-contain"
			src="https://masai-website-images.s3.ap-south-1.amazonaws.com/logo.png"
			alt="masai logo"
		/>
		<div class="flex justify-between items-center gap-5">
			<button class=" p-2 hover:bg-slate-50 text-sm hover:text-[#ec0532] hover:rounded-md"
				>COURSE</button
			>
			<button class=" p-2 hover:bg-slate-50 text-sm hover:text-[#ec0532] hover:rounded-md"
				>FEES</button
			>
			<button class=" p-2 hover:bg-slate-50 text-sm hover:text-[#ec0532] hover:rounded-md"
				>EVENTS</button
			>
			<button class=" p-2 hover:bg-slate-50 text-sm hover:text-[#ec0532] hover:rounded-md"
				>LEARN</button
			>
			<button class="p-2 rounded-md text-[#ec0532] bg-slate-50 text-md">SUCCESS STORIES</button>
			<button class=" p-2 hover:bg-slate-50 text-sm hover:text-[#ec0532] hover:rounded-md"
				>HIRE FROM US</button
			>
		</div>
		<div class="flex justify-center items-center gap-2">
			<button class="text-sm text-[#898fd7] p-4 rounded-lg bg-[#e5fefe]">REFER & EARN</button>
			<button
				on:click={toggleSidebar}
				class="text-sm border border-[#ec0532] text-[#ec0532] border-1 p-4 rounded-lg"
				>SIGN UP</button
			>
		</div>
	</div>
	{#if isOpen}
		<div
			class="fixed flex flex-col  p-5 top-0 right-0 h-screen w-full md:w-1/3 bg-[#ffffff] transform scale-70 shadow-lg"
		>
			<!-- Sidebar content goes here -->

			<div class="flex justify-end">
				<button class="text-[#ec0532] hover:bg-slate-50 p-4" on:click={toggleSidebar}
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
			<Signup />
		</div>
	{/if}
</main>
