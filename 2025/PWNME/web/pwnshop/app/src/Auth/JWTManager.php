<?php
namespace App\Auth;

use Firebase\JWT\JWT;
use Firebase\JWT\Key;
use Exception;

class JWTManager {
    private string $key;
    private string $algorithm;

    public function __construct() {
        $this->key = 'ThisIsNotTheSameSecretOnRemote';
        $this->algorithm = 'HS256';
    }

    public function generateToken(array $user): ?string {
        try {
            $payload = [
                'user_id' => $user['id'],
                'username' => $user['username'],
                'permissions' => $user['permissions'],
                'iat' => time(),
                'exp' => time() + 3600
            ];

            return JWT::encode($payload, $this->key, $this->algorithm);
        } catch (Exception $e) {
            return null;
        }
    }

    public function validateToken(?string $token): ?array {
        if (!$token) {
            return null;
        }

        try {
            $decoded = JWT::decode($token, new Key($this->key, $this->algorithm));
            return [
                'user_id' => $decoded->user_id,
                'username' => $decoded->username,
                'permissions' => $decoded->permissions
            ];
        } catch (Exception $e) {
            return null;
        }
    }
}
