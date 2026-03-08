import asyncio
from playwright.async_api import async_playwright

BASE_URL = "https://utdallas.t2hosted.com"
AUTH_GUEST = "/cmn/auth_guest.aspx"
ACCOUNT_PORTAL = "/Account/Portal"
ACCOUNT_CITATIONS = "/Account/Citations/Results"

GUEST_SIGN_IN_ROUTE = f"{BASE_URL}/cmn/auth_guest.aspx"
GUEST_SIGN_UP_ROUTE = f"{BASE_URL}/cmn/newuser.aspx"
ACCOUNT_PORTAL_ROUTE = f"{BASE_URL}/Account/Portal"
ACCOUNT_CITATIONS_ROUTE = f"{BASE_URL}/Account/Citations/Results"

async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            slow_mo=100,
        )
        device = p.devices.get("Desktop Chrome")
        context = await browser.new_context(
            **device,
            base_url=BASE_URL,
        )
        context.set_default_timeout(0)

        # await handle_captcha_parallel(context=context, num_tabs=10)
        # await sign_in(context)
        # await processAllDevices(context)
        
        await asyncio.sleep(30)
        await context.close()
        await browser.close()
        print("Finished")



if __name__ == "__main__":
    asyncio.run(main())
