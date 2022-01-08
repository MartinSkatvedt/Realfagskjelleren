from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        claims['email'] = request.user.email
        claims['username'] = request.user.username
        claims['first_name'] = request.user.first_name
        claims['last_name'] = request.user.last_name
        return claims
    
