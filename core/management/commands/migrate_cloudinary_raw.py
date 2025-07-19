from django.core.management.base import BaseCommand
from cloudinary.uploader import upload
from core.models import OldPaper, Project
from django.core.files.base import ContentFile
import requests


class Command(BaseCommand):
    help = "Migrate PDFs and ZIPs to Cloudinary as 'raw' resources."

    def handle(self, *args, **kwargs):
        self.migrate_old_papers()
        self.migrate_projects()

    def migrate_old_papers(self):
        self.stdout.write(self.style.NOTICE("\n🔄 Migrating OldPaper files..."))
        papers = OldPaper.objects.all()
        for paper in papers:
            if not paper.file:
                self.stdout.write(f"❌ Skipping {paper.title}: No file found.")
                continue
            try:
                self.stdout.write(f"⬇️  Downloading: {paper.file.url}")
                res = requests.get(paper.file.url)
                if res.status_code != 200:
                    self.stdout.write(f"⚠️  Failed to download: {paper.file.url}")
                    continue

                result = upload(ContentFile(res.content), resource_type="raw")
                paper.file.name = result["public_id"] + "." + result["format"]
                paper.save()
                self.stdout.write(self.style.SUCCESS(f"✅ Updated {paper.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error: {e}"))

    def migrate_projects(self):
        self.stdout.write(self.style.NOTICE("\n🔄 Migrating Project zip files..."))
        projects = Project.objects.all()
        for project in projects:
            if not project.zip_file:
                self.stdout.write(f"❌ Skipping {project.title}: No zip file found.")
                continue
            try:
                self.stdout.write(f"⬇️  Downloading: {project.zip_file.url}")
                res = requests.get(project.zip_file.url)
                if res.status_code != 200:
                    self.stdout.write(f"⚠️  Failed to download: {project.zip_file.url}")
                    continue

                result = upload(ContentFile(res.content), resource_type="raw")
                project.zip_file.name = result["public_id"] + "." + result["format"]
                project.save()
                self.stdout.write(self.style.SUCCESS(f"✅ Updated {project.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error: {e}"))
