<?php declare(strict_types=1);

namespace App\Controller;

// $value precisa ser uma string para iniciar valores com 0, como 01 por exemplo.
abstract class AbstractController {
    public function render(string $viewName, string $result = null): void {
        require_once "../src/Views/_partials/header.php";
        require_once "../src/Views/{$viewName}.php";
        require_once "../src/Views/_partials/footer.php";
    }
}
