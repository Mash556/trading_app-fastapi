from fastapi import APIRouter, Depends, BackgroundTasks
from .tasks import send_email_report_dashboard
from auth.base_config import current_user

router = APIRouter(prefix='/report')

@router.get('/dashboard')
def get_dashboard_report(backround_task: BackgroundTasks, user=Depends(current_user)):
    # backround_task.add_task(send_email_report_dashboard, user.username)
    # send_email_report_dashboard(user.username)
    send_email_report_dashboard.delay(user.username)
    return {
        'status': 'success',
        'data': 'письмо отправлено',
        'detail': None
        }