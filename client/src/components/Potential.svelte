<script>
	let ind = 0;
	const obj = [
		{
			id: 1,
			name: 'Ramendra Vikram Singh Parihar',
			image: 'https://masaischool.com/images/new-homepage/banner-student-image3.webp',
			description:
				'Going through the 11-11-6 curriculum was a breathtaking experience. Every new unit came with great enthusiasm and a new challenge.',
			companyLogo: 'https://masaischool.com/images/new-homepage/company-logo3.svg'
		},
		{
			id: 2,
			name: 'Salman Lukhman Shaikh',
			image: 'https://masaischool.com/images/new-homepage/banner-student-image4.webp',
			description: 'I learnt a lot from Masai i.e discipline, time management and professionalism.',
			companyLogo: 'https://masaischool.com/images/new-homepage/company-logo4.svg'
		},
		{
			id: 3,
			name: 'Harshit Tripathi',
			image: 'https://masaischool.com/images/new-homepage/banner-student-image1.webp',
			description:
				'I liked that every thing is taught in a structured manner, and there is no spoon feeding. That helps us learn by ourself when we do.',
			companyLogo: 'https://masaischool.com/images/new-homepage/company-logo1.svg'
		},
		{
			id: 4,
			name: 'Puja Kumari',
			image: 'https://masaischool.com/images/new-homepage/banner-student-image2.webp',
			description:
				'I developed Communication Skills, People Skills, Mindset, active patience, JAVA, DSA, JavaScript, CSS, and HTML.',
			companyLogo: 'https://masaischool.com/images/new-homepage/company-logo2.svg'
		}
	];

	function nextSlide() {
		ind = (ind + 1) % obj.length;
		setTimeout(nextSlide, 10000);
	}

	import { onMount } from 'svelte';
	onMount(() => {
		setTimeout(nextSlide, 10000);
	});
</script>

<div class="">
	<div class="bg-[#FCFAFA] mb-[130px] lg:mb-[0px] lg:pr-[30px]">
		<div class="max-w-[1280px] mx-auto py-[40px] lg:py-[32px] px-[16px] xl:px-[0px]">
			<div
				class="lg:min-h-[472px] grid lg:flex justify-center lg:justify-between text-center lg:text-left"
			>
				<div class="my-auto">
					<div class="w-[100%]">
						<h1
							class="font-[700] text-[48px] leading-[62px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !font-[700] lg:!font-[800] !text-[24px] lg:!text-[48px] !leading-[32px] lg:!leading-[62px] !inline !text-[#000000]"
						>
							Realise Your Potential
							<div class="hidden md:inline"><br /></div>

							With
						</h1>
						<div class="inline isolate">
							<h1
								class="font-[700] text-[48px] leading-[62px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 relative whitespace-nowrap !font-[700] lg:!font-[800] !text-[24px] lg:!text-[48px] !inline !text-[#ED0331] !leading-[32px] lg:!leading-[62px] isolate"
							>
								Assured Outcomes
								<img
									class="absolute z-[-1] left-0 right-0 bottom-[-15px] md:bottom-[-12px] w-[90%] mx-auto h-[30px]"
									src="https://masaischool.com/images/new-homepage/yellow-vector.svg"
									alt="yellow vector"
								/>
							</h1>
						</div>
						<div class="hidden md:inline"><br /></div>
						<h1
							class="font-[700] text-[48px] leading-[62px] font-poppins transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !font-[700] lg:!font-[800] !text-[24px] lg:!text-[48px] !leading-[32px] lg:!leading-[62px] !inline text-[#000000]"
						>
							Delivered.
						</h1>
					</div>
					<p
						class="!font-[400] text-[24px] leading-[34px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !text-[#21191B] mt-[12px] lg:mt-[16px]"
					>
						India’s only outcome-based career institute.
						<br class="hidden lg:block" /> Enter the tech workforce industry-ready.
					</p>
					<button
						type="button"
						class="active:!ring-0 bg-ms-red-500 hover:bg-ms-red-600 rounded-[8px] text-white !font-[600] text-[14px] leading-[24px] font-sans tracking-[1.25px] uppercase p-[12px_16px] inline-block focus:!ring-0 outline-offset-[5px] outline-[1px] outline-[transparent] focus-visible:!shadow-[0_0_0_3px_rgba(66,_153,_225,_0.6)] disabled:opacity-[0.6] disabled:cursor-not-allowed transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 rounded-[8px] min-h-[48px] uppercase leading-[24px] text-[18px] font-[600] hover:bg-ms-red-600 bg-[#ED0331] text-[#fff] !mt-[24px] !lg:mt-[32px] !py-[12px] !px-[20px]"
						>Get your dream job
					</button>
				</div>
				<div class="relative lg:mb-[-32px] mt-[64px] lg:mt-auto h-[100%]">
					<div class="max-w-[382px] lg:max-w-[100%] mx-auto">
						<div
							class="relative"
							style="animation: 0.5s ease-in-out 0s 1 normal none running fadeIn;"
						>
							<div
								class="absolute h-[100%] w-[100%] md:w-full md:h-full scale-[0.95] rounded-[40px] rotate-[-7deg] md:rotate-[-15deg] border border-[#3470E4]"
							/>
							<div
								class="min-h-[399px] lg:min-h-[499px] xl:min-h-[502px] relative pt-[30px] md:pt-[64px] mt-auto flex rounded-tr-[20px] bg-[#D6E2FA] rounded-tl-[20px]"
							>
								<img
									class="mx-auto bottom-[-2px] w-fit lg:w-[424px] !relative max-h-[335px] lg:max-h-[435px]"
									src={obj[ind].image}
									alt="new homepage"
								/>
								<div
									class="flex-row flex min-h-[196px] md:min-h-[198px] text-left p-[16px] rounded-[24px] absolute xl:max-w-[455px] left-[0px] xl:left-[-70%] z-1 bottom-[-40%] lg:bottom-[0px] xl:bottom-[40px]"
									style="box-shadow:0px 4px 7px 0px #BDBDBD40;background:linear-gradient(181.98deg, rgba(245, 245, 245, 0.9) 1.36%, rgba(255, 255, 255, 0.9) 99.56%)"
								>
									<div>
										<img
											src="https://masaischool.com/images/new-homepage/quote-start.svg"
											alt="quote"
											class="mr-[4px] mt-[-18px] inline min-w-[19px]"
											style=""
										/>
									</div>
									<div class="flex flex-col gap-[4px]">
										<div>
											<p
												class="!font-[600] text-[14px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 !inline !text-[#21191B]"
											>
												{obj[ind].description}
											</p>
											<img
												src="https://masaischool.com/images/new-homepage/quote-end.svg"
												alt="quote"
												class="mt-[-12px] inline min-w-[19px]"
												style=""
											/>
										</div>
										<div class="flex-1 flex flex-col justify-end items-start gap-[5px]">
											<p
												class="!font-[400] text-[16px] leading-[24px] font-sans transition-[background-color,border-color,color,fill,stroke,opacity,box-shadow,transform] duration-200 undefined"
											>
												{obj[ind].name}
											</p>
											<img
												src={obj[ind].companyLogo}
												alt="company logo"
												class="mt-[4px] h-[32px]"
												style=""
											/>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
