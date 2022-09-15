<?php declare(strict_types=1);

use App\Controller\IndexController;

function createRoute(string $controllerName, string $methodName): array {
    return [
        "Controller" => $controllerName,
        "Method" => $methodName,
    ];
}

$routes = [
    "/" => createRoute(IndexController::class, "index"),
];

return $routes;
