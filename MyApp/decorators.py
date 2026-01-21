from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("Silakan login terlebih dahulu.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def mahasiswa_602_required(f):
    """Decorator untuk hak akses Mahasiswa 602 (Data Pelanggan)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("Silakan login terlebih dahulu.", "warning")
            return redirect(url_for('login'))
        
        user_role = session.get('role')
        if user_role != 'mahasiswa_602':
            flash("Akses ditolak: Hanya Mahasiswa 602 yang dapat mengakses form ini.", "danger")
            return redirect(url_for('home'))
        
        return f(*args, **kwargs)
    return decorated_function


def mahasiswa_614_required(f):
    """Decorator untuk hak akses Mahasiswa 614 (Data Barang)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("Silakan login terlebih dahulu.", "warning")
            return redirect(url_for('login'))
        
        user_role = session.get('role')
        if user_role != 'mahasiswa_614':
            flash("Akses ditolak: Hanya Mahasiswa 614 yang dapat mengakses form ini.", "danger")
            return redirect(url_for('home'))
        
        return f(*args, **kwargs)
    return decorated_function