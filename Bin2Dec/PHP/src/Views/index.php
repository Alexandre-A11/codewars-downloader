<main class="bg-conic-to-b from-sky-400 to-blue-800 h-screen flex">
    <div id="left" class="w-full flex flex-col">
        <a href="https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Bin2Dec-App.md" target="_blank">
            <h1 class="font-bold text-6xl text-sky-400 hover:-translate-y-1 drop-shadow-xl text-center relative mt-12">Bin2Dec</h1>
        </a>
        <a href="https://github.com/florinpop17/app-ideas" target="_blank">
            <h2 class="font-bold text-center mt-6 text-4xl text-yellow-400 hover:translate-x-1">App Ideias</h2>
        </a>
        <p class="text-lg self-center mt-6 text-sky-100 w-4/6"><span class="font-bold">Bin2Dec</span> permite o usuário digitar até 8 dígitos binários, 0 e 1, em sequência mostra o valor decimal equivalente. </p>

        <form method="post" class="h-1/2 mt-12 grid place-content-center">
            <div class="max-w-lg mb-6">
                <input type="text" name="binary" maxlength="8" oninput="this.value = this.value.replace(/[^0-1.]/g, '');" required placeholder="Digite o código binário" class="cursor-pointer shadow-xl rounded-lg py-6 px-4 bg-white w-full text-lg text-center placeholder-gray-400 outline-none" />
            </div>

            <button type="submit" class="rounded-lg css-button-3d--black">Converter para Decimal</button>
        </form>
    </div>
    <div id="right" class="w-full grid place-content-center">
        <div class="top-5 ml-10 absolute font-bold text-4xl translate-y-4 text-sky-100">
            <?php echo $_POST ? $_POST["binary"] : null; ?>
        </div>
        <div class="text-center font-bold text-9xl translate-y-4 text-slate-800">
            <?php echo isset($result) ? $result : "Decimal"; ?>
        </div>
    </div>
</main>

<!-- Código necessário para não fazer o reenvio do post ao dar refresh na página -->
<script>
    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }
</script>