<?php declare(strict_types=1);

namespace App\Controller;

abstract class AbstractController {
    public function render(string $viewName): void {
        require_once "../src/Views/_partials/header.php";
        require_once "../src/Views/{$viewName}.php";
        require_once "../src/Views/_partials/footer.php";
    }
}
