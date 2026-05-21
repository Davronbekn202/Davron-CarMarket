from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


def send_reset_password_email(email, code):
    html_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Reset</title>
    </head>
    <body style="margin:0;padding:0;background:#0a0a0a;font-family:Arial,sans-serif;">

        <table width="100%" cellpadding="0" cellspacing="0" style="background:#0a0a0a;padding:40px 0;">
            <tr>
                <td align="center">
                    <table width="520" cellpadding="0" cellspacing="0" style="width:520px;max-width:100%;">

                        <!-- Logo -->
                        <tr>
                            <td align="center" style="padding-bottom:28px;">
                                <table cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td style="background:#c9a84c;border-radius:6px;padding:8px 12px;vertical-align:middle;">
                                            <span style="font-size:11px;font-weight:bold;color:#0a0a0a;letter-spacing:3px;text-transform:uppercase;">&#9679; DAVRON</span>
                                        </td>
                                        <td style="padding-left:10px;vertical-align:middle;">
                                            <span style="font-size:18px;font-weight:bold;color:#f0ece4;letter-spacing:3px;text-transform:uppercase;">CAR MARKET</span>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Card -->
                        <tr>
                            <td style="background:#111111;border-radius:12px;border:1px solid rgba(255,255,255,0.07);overflow:hidden;">

                                <!-- Card header -->
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td style="background:#161616;padding:32px 40px 28px;border-bottom:1px solid rgba(201,168,76,0.15);">
                                            <p style="margin:0 0 8px;font-size:10px;font-weight:bold;letter-spacing:3px;text-transform:uppercase;color:#c9a84c;">Account Security</p>
                                            <h1 style="margin:0;font-size:32px;letter-spacing:2px;color:#f0ece4;line-height:1;font-weight:bold;">Password Reset</h1>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Card body -->
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td style="padding:36px 40px;">

                                            <p style="margin:0 0 24px;font-size:15px;color:#8a8680;line-height:1.7;">
                                                We received a request to reset the password for your account. Use the one-time code below to proceed.
                                            </p>

                                            <!-- OTP Box -->
                                            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
                                                <tr>
                                                    <td align="center" style="background:#0a0a0a;border:1px solid rgba(201,168,76,0.3);border-radius:8px;padding:28px 20px;">
                                                        <p style="margin:0 0 8px;font-size:10px;font-weight:bold;letter-spacing:3px;text-transform:uppercase;color:#5a5550;">Your OTP Code</p>
                                                        <p style="margin:0;font-size:42px;font-weight:bold;letter-spacing:12px;color:#c9a84c;">{code}</p>
                                                    </td>
                                                </tr>
                                            </table>

                                            <!-- Warning -->
                                            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:28px;">
                                                <tr>
                                                    <td style="background:rgba(192,57,43,0.08);border:1px solid rgba(192,57,43,0.2);border-radius:6px;padding:14px 18px;">
                                                        <p style="margin:0;font-size:13px;color:#e74c3c;line-height:1.6;">
                                                            &#9888;&nbsp; This code expires in <strong>10 minutes</strong>. If you did not request a password reset, please ignore this email.
                                                        </p>
                                                    </td>
                                                </tr>
                                            </table>

                                            <p style="margin:0;font-size:13px;color:#5a5550;line-height:1.7;">
                                                For security, never share this code with anyone. Davron Car Market will never ask for your OTP via phone or chat.
                                            </p>

                                        </td>
                                    </tr>
                                </table>

                                <!-- Card footer -->
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td style="padding:20px 40px 28px;border-top:1px solid rgba(255,255,255,0.04);">
                                            <p style="margin:0;font-size:12px;color:#3a3530;text-align:center;">
                                                &copy; 2025 Davron Car Market &mdash; Tashkent, Uzbekistan
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                            </td>
                        </tr>

                    </table>
                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    plain_message = f"Your OTP code is: {code}"

    msg = EmailMultiAlternatives(
        subject="Password Reset OTP — Davron Car Market",
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )
    msg.attach_alternative(html_message, "text/html")
    msg.send(fail_silently=False)
