import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from simple_notifications.cli import pushover, pushbullet, email
import os

class TestNotifications(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        os.environ['LC_ALL'] = 'en_US.UTF-8'
        os.environ['LANG'] = 'en_US.UTF-8'

    
    def test_help():
        runner = CliRunner()
        result = runner.invoke(cli.notification)
        assert result.exit_code == 0
        assert "Usage: " in result.output

    
    @patch('simple_notifications.cli.simple_notifications_config.PUSHOVER_APP_TOKEN', 'fake_token')
    @patch('simple_notifications.cli.simple_notifications_config.USER_KEY', 'fake_user_key')
    @patch('requests.post')
    def test_pushover(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200)
        result = self.runner.invoke(pushover, ['--subject', 'Test Subject', '--body', 'Test Body', '--image', 'no'])
        print("Output:", result.output)  # Debugging output
        print("Exception:", result.exception)  # Print exception if any
        print("Exit Code:", result.exit_code)  # Print exit code
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Sending out Pushover notification...', result.output)
        self.assertIn('Sending complete.', result.output)

    
    @patch('simple_notifications.cli.simple_notifications_config.PUSHBULLET_APP_TOKEN', 'fake_token')
    @patch('requests.post')
    def test_pushbullet(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200)
        result = self.runner.invoke(pushbullet, ['--subject', 'Test Subject', '--body', 'Test Body'])
        print("Output:", result.output)  # Debugging output
        print("Exception:", result.exception)  # Print exception if any
        print("Exit Code:", result.exit_code)  # Print exit code
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Sending out Pushbullet notification...', result.output)
        self.assertIn('Sending complete.', result.output)

    
    @patch('simple_notifications.cli.simple_notifications_config.EMAIL_SENDER', 'test@example.com')
    @patch('simple_notifications.cli.simple_notifications_config.EMAIL_SERVER', 'smtp.example.com')
    @patch('simple_notifications.cli.simple_notifications_config.EMAIL_SERVER_PORT', '587')
    @patch('simple_notifications.cli.simple_notifications_config.EMAIL_PASSWORD', 'fake_password')
    @patch('smtplib.SMTP')
    def test_email(self, mock_smtp):
        mock_smtp_instance = mock_smtp.return_value
        result = self.runner.invoke(email, ['--subject', 'Test Subject', '--body', 'Test Body', '--recipients', 'test@example.com'])
        print("Output:", result.output)  # Debugging output
        print("Exception:", result.exception)  # Print exception if any
        print("Exit Code:", result.exit_code)  # Print exit code
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Sending out Email notification...', result.output)
        self.assertIn('Sending complete.', result.output)
        mock_smtp_instance.sendmail.assert_called_once()


if __name__ == '__main__':
    unittest.main()
